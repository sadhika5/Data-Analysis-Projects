# Transforming Data with Python

This folder contains files created/used for the  project at www.dataquest.io. The purpose of this exercise is to write scripts that 
import functions from other python files and then execute them on the command line.


Analysis of a dataset of submissions to Hacker News from 2006 to 2015

Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), 
and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular 
it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

### hn_stories.csv
##### This csv file contains all the data that will be worked on
### read.py
##### This script includes the function to read the csv file and assign it to a dataframe with the addition of column names to the file
### count.py
##### This script includes the seperation of the strings  and prints the most common 100 words  in the dataframe
### domains.py
##### This script will print the 100 most common  domains that are submitted
### times.py
##### This script includes the dateutil.parser function to output a datetime object from the timestamp 
