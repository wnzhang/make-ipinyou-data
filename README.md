make-ipinyou-data
=================

This project is to formalise the iPinYou RTB data into a standard format for further researches.

### Step 0
Go to [data.computational-advertising.org](http://data.computational-advertising.org) to download `ipinyou.contest.dataset.zip`. Unzip it and get the folder `ipinyou.contest.dataset`.

### Step 1
Update the soft link for the folder `ipinyou.contest.dataset` in `original-data`. 
```
weinan@ZHANG:~/Project/make-ipinyou-data/original-data$ ln -sfn ~/Data/ipinyou.contest.dataset ipinyou.contest.dataset
```
Under `make-ipinyou-data/original-data/ipinyou.contest.dataset` there should be the original dataset files like this:
```
weinan@ZHANG:~/Project/make-ipinyou-data/original-data/ipinyou.contest.dataset$ ls
algo.submission.demo.tar.bz2  README         testing2nd   training3rd
city.cn.txt                   region.cn.txt  testing3rd   user.profile.tags.cn.txt
city.en.txt                   region.en.txt  training1st  user.profile.tags.en.txt
files.md5                     testing1st     training2nd
```
You do not need to further unzip the packages in the subfolders.

### Step 2
Under `make-ipinyou-data` folder, just run `make all`.
After the program finished, the total size of the folder will be 8.1G.

For any questions, please report the issues or contact Weinan Zhang. Email: w.zhang@cs.ucl.ac.uk
