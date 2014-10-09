advertisers="1458 2261 2997 3386 3476 2259 2821 3358 3427"

for advertiser in $advertisers; do
    echo $advertiser
    python python/mkyzx.py $advertiser/train.log.txt $advertiser/test.log.txt $advertiser/train.yzx.txt $advertiser/test.yzx.txt $advertiser/featindex.txt
done

