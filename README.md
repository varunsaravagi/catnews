catnews
=======

I wrote this python script to replace images in the tweets with cat pictures.

Usage
=======
Delete the text fron the <code>since_id.txt</code> file for the initial run. In the subsequent runs, this file would contain the id of the last read tweet and would read the tweets after that.

<code> python catnews.py <i>handle count</i> </code> 

This would read the given number of tweets (count) from the given handle and if the tweets have an image embedded, would replace it with a random cat image.

Subsequent runs would read the tweets from the last read tweet.

The keys required by twitter are in a separate file which has been imported in the main script. Please give your keys in order to run the script


