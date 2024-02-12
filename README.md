# Coronavirus Twitter Analysis

In this project I scanned all the geotagged tweets sent in 2020 to monitor for the spread of coronoavirus on social media.

Some of the skills involved included: 
1. working with a large scale dataset (1.1 billion tweets)
2. working with multilingual text
3. using the MapReduce divide-and-conquer paradigm to create parallel code
4. Visualizing data

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
I gained access to all the geotagged tweets sent in 2020 and stored them as followed:

The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format.



## Procedure

### MapReduce:
The first step I took to analyze the tweets was using a [Mapping](https://en.wikipedia.org/wiki/MapReduce) procedure
It is a 3 step procedure summarized in the following image:

<img src=mapreduce.png width=100% />
The partition step is done by breaking the dataset into smaller files for each day.


#### Mapping

Let $n$ be the size of the dataset and $p$ be the number of processors used to do the computation.
The simplest and most common scenario is that the map procedure takes time $O(n/p)$ 
Using a mapping function, I was able to create files for each day that had information on the countries and languages of each tweet.

#### Reducing

The reducing procedure is a function that takes time $O(1)$ The reducing step involved combining the data from the mapping step to produce one file with country data and one for language data.

## Visualization

After acquiring the data from the map reduce step, I wrote a python function, visualize.py to create plots demonstrating the different data. The first visuals I created was seeing the top 10 countries that used the hashtag `#coronavirus` and `#코로나바이러스` in 2020. After that I visualized the top 10 languages for tweets that used the same hashtags. The plots are shown below:

**Tweets by country for #coronavirus in 2020**
<img src=coronaviruscountry.png width=100% />
**Tweets by country for #코로나바이러스 in 2020**
<img src=코로나바이러스country.png width=100% />
**Tweets by language for #coronavirus in 2020**
<img src=coronaviruslang.png width=100% />
**Tweets by language for #코로나바이러스 in 2020**
<img src=코로나바이러스lang.png width=100% />


## Alternative Reduce
The last task I worked on was creating a new file `alternative_reduce.py` that would allow me to compare different hashtags over the course of 2020. The file allows for a list of hastags and generates a plot where:
1. There is one line per input hashtag.
2. The x-axis is the day of the year.
3. The y-axis is the number of tweets that use that hashtag during the year.

Using this method, I created a visualization of 4 different hastags: #sick, #flu, #cough, and #sneeze
This is shown in the graph below:
<img src=sick_flu_cough_sneeze.png width=100% />




