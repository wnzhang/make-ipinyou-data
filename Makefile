
# makefile to create ipinyou dataset evaluation
BASE=.
ORIGINALFOLDER=./original-data/ipinyou.contest.dataset
TRAIN=$(ORIGINALFOLDER)/train
TEST=$(ORIGINALFOLDER)/test

all: init clk train.log test.log advertisers yzx

init: $(ORIGINALFOLDER)
	mkdir -p $(TRAIN)
	cp $(ORIGINALFOLDER)/training2nd/imp.*.bz2 $(TRAIN)
	cp $(ORIGINALFOLDER)/training2nd/clk.*.bz2 $(TRAIN)
	cp $(ORIGINALFOLDER)/training3rd/imp.*.bz2 $(TRAIN)
	cp $(ORIGINALFOLDER)/training3rd/clk.*.bz2 $(TRAIN)
	bzip2 -d $(TRAIN)/*
	mkdir -p $(TEST)
	cp $(ORIGINALFOLDER)/testing2nd/* $(TEST)
	cp $(ORIGINALFOLDER)/testing3rd/* $(TEST)
	bzip2 -d $(TEST)/*
	mkdir $(BASE)/all	

clk: $(TRAIN)
	cat $(TRAIN)/clk*.txt > $(BASE)/all/clk.all.txt

train.log: $(BASE)/schema.txt $(BASE)/all/clk.all.txt 
	cat $(TRAIN)/imp*.txt | $(BASE)/python/mkdata.py $+ > $(BASE)/all/train.log.txt
	$(BASE)/python/formalizeua.py $(BASE)/all/train.log.txt

test.log: $(BASE)/schema.txt
	cat $(TEST)/*.txt | $(BASE)/python/mktest.py $+ > $(BASE)/all/test.log.txt
	$(BASE)/python/formalizeua.py $(BASE)/all/test.log.txt

advertisers: $(BASE)/all/train.log.txt $(BASE)/all/test.log.txt
	$(BASE)/python/splitadvertisers.py $(BASE) 25 $(BASE)/all/train.log.txt $(BASE)/all/test.log.txt

yzx: advertisers
	bash $(BASE)/mkyzxdata.sh


