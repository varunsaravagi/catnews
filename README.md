catnews
=======

I wrote this python script to replace images in the tweets with cat pictures.

Usage
=======

<code> python catnews.py </code> 

Delete the text fron the <code>since_id.txt</code> file for the initial run. In the subsequent runs, this file would contain the id of the last read tweet and would read the tweets after that.
Enter the handles, one in each line, foe which the script is to be run un <code>users.txt</code> file. 

Subsequent runs would read the tweets from the last read tweet.

The keys required by twitter are in a separate file which has been imported in the main script. Please give your keys in order to run the script


