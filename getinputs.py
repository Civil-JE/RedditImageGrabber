# # #
# Author: Josh Eastman
# Updated: 02/16/18
# Version 1.0.0
# Description: Input control/verification file for RedditImageGrabber.
# # #

from prawcore import NotFound
import time


# Check if a subreddit exists.
def does_sub_exist(sub, reddit):
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists


# Check if doing default search for predefined values. Custom search for w.e they need
def get_grab_type():
    grab_type = None
    while grab_type is None:
        grab_type_i = input('Would you like to do a default search? (Y/N)\n')
        if grab_type_i.lower() == 'y' or grab_type_i == 'n':
            grab_type = grab_type_i.lower()
        else:
            continue
    return grab_type


# Get Subreddit. Make sure it exists
def get_subreddit(reddit):
    sub_exists = False
    subreddit = None
    while not sub_exists:
        subreddit = input('Choose your subreddit: (Do not include /r/)\n')
        sub_exists = does_sub_exist(subreddit, reddit)
        if not sub_exists:
            print('Subreddit not found. Try again')
            time.sleep(1)
    return subreddit


# Get Number of posts to download
def get_number_of_posts():
    # Get number of posts
    is_num = False
    number_of_posts = None
    while not is_num:
        number_of_posts = input('How many posts would you like?\n')
        try:
            number_of_posts = int(number_of_posts)
            is_num = True
        except:
            print('Not a valid number. Try again')
            time.sleep(1)
    return number_of_posts


# How to sort the subreddit
def get_sort_by():
    is_valid = False
    sort_by = None
    while not is_valid:
        sort_by = input('How would you like to sort the Subreddit? (Hot/Top/New)\n')
        sort_by = sort_by.lower()
        if sort_by == 'hot' or sort_by == 'top' or sort_by == 'new':
            is_valid = True
        else:
            print('Type not found. Try again')
            time.sleep(1)

    return sort_by


# What time frame to search in
# week, day, month, year, hour, all
def get_sort_time():
    is_valid = False
    sort_time = None
    while not is_valid:
        sort_time = input('What time frame would you like to search in? (All, Month, Week, Day, Year, Hour)\n')
        sort_time = sort_time.lower()
        if (sort_time == 'all' or sort_time == 'year' or sort_time == 'month' or sort_time == 'week'
                or sort_time == 'day' or sort_time == 'hour'):
            is_valid = True
        else:
            print('Not a valid time frame. Try again')
            time.sleep(1)
    return sort_time


def get_required_values(reddit):
    subreddit = None
    number_of_posts = None
    sort_by = None
    sort_time = None
    grab_type = get_grab_type()

    if grab_type == 'n':
        subreddit = get_subreddit(reddit)
        number_of_posts = get_number_of_posts()
        sort_by = get_sort_by()
        if sort_by == 'top':
            sort_time = get_sort_time()

    return [grab_type, subreddit, number_of_posts, sort_by, sort_time]
