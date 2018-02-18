####
# Author: Josh Eastman
# Updated: 02/16/18
# Version 1.0.0
# Description: Main file for RedditImageGrabber.
####
from instance import *
from getinputs import *
from link_image_handling import *
import logging

logging.basicConfig(filename='redditImageGrab.log', format='%(levelname)s:%(asctime)s:%(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.INFO)

IMAGE_DIRECTORY = 'images/'   # Change 'images/' to your preferred image storage location

DEFAULT_VALUES = ['y', 'pics', 25, 'hot', None]  # Values used when default search chosen
# [grab_type, subreddit, number_of_posts, sort_by, sort_time]

reddit = RedditInstance().reddit_instance

# Get Required Values
required_values = get_required_values(reddit)

# Set Required Values
if required_values[0] == 'y':
    required_values = DEFAULT_VALUES
    
subreddit = required_values[1]
number_of_posts = required_values[2]
sort_by = required_values[3]
sort_time = required_values[4]

print('Working...')

# Pick the path based on chosen Sort_by
if sort_by == 'hot':
    for idx, submission in enumerate(reddit.subreddit(subreddit).hot(limit=number_of_posts)):
        try:
            download_all(submission, IMAGE_DIRECTORY)
        except:
            logging.info('Failed to get image. | ' + submission.url + ' | ' + submission.title)
elif sort_by == 'top':
    for idx, submission in enumerate(reddit.subreddit(subreddit).top(sort_time, limit=number_of_posts)):
        try:
            download_all(submission, IMAGE_DIRECTORY)
        except:
            logging.info('Failed to get image. | ' + submission.url + ' | ' + submission.title)
elif sort_by == 'new':
    for idx, submission in enumerate(reddit.subreddit(subreddit).new(limit=number_of_posts)):
        try:
            download_all(submission, IMAGE_DIRECTORY)
        except:
            logging.info('Failed to get image. | ' + submission.url + ' | ' + submission.title)

try:
    sort_downloads(IMAGE_DIRECTORY)
except:
    logging.ERROR('Failed to sort images')
