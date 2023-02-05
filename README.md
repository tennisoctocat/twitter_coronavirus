# Coronavirus twitter analysis

This project uses the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) programming model to process all geotagged tweets sent in 2020. In particular, the project determines the number of tweets of each language and country that contain the hashtags `#coronavirus` and `#코로나바이러스`. This is part of a [Big Data (CSCI 143) homework assignment](https://github.com/mikeizbicki/cmc-csci143/tree/2023spring/topic_01_mapreduce/homework).

## Results

Using this process, we create graphs showing the top 10 countries and languages with `#coronavirus` and `#코로나바이러스`. Here are the results:

<img src=./graphs/reduced.country%23coronavirus.png width=100%/>
<img src=./graphs/reduced.lang%23coronavirus.png width=100%/>
<img src=./graphs/reduced.country%23코로나바이러스.png width=100%/>
<img src=./graphs/reduced.lang%23코로나바이러스.png width=100%/>

## Running the Code

In order to run this code, you need to be on the CMC lambda server. If you do have access to the server, here are the commands to run the MapReduce algorithm using this repository:

Run this command to run the map script on all tweets from 2020 and keep the script running even after you logout of the lambda server. `run_maps.sh` is a shell script which runs `map.py` on the tweets for every day in 2020. `map.py` process the tweets for a single day and outputs JSON formatted information about the tweets in that day. 
```
$ nohup ./run_maps.sh &
```

Reduce the outputs for all of the days into a single output files with these two commands. They contain JSON formatted information about tweets grouped by language for the first command and country for the second.
```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
$ ./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country
```

Visualize the top 10 countries with tweets containing a given hashtag with 
```
$ ./src/visualize.py --input_path=reduced.country --key=HASHTAG
```

Or the top 10 languages with tweets containing a given hashtag with 
```
$ ./src/visualize.py --input_path=reduced.lang --key=HASHTAG
```

The above two commands will output images into the `graphs` directory, which can then be pushed to github and viewed. 

