###
# Author: Josh Eastman
# Updated: 02/16/18
# Version 1.0.0
# Description: Based on link_image_handling from TwitterArtBot. Used to deal with the link provided
# by PRAW and download the images.
###
import urllib.request
import os
import logging


# If a link does not have .jpg at the end, add it
def if_no_extension_add(url):
    if url[-4:] != '.jpg' and url[-4:] != '.png':
        new_url = url + '.jpg'
        return new_url
    else:
        return url


def handle_link(url):
    # Check if imgur or reddit
    # To-Do: Add more sites for better compatibility
    try:
        # Checks for the various states the imgur url can come in
        if url.find('i.imgur') != -1:
            fixed_url = if_no_extension_add(url)
            image = fixed_url[20:]  # for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image]  # boolean for whether or not it failed

        elif url.find('imgur') != -1:
            jpg_url = if_no_extension_add(url)
            fixed_url = jpg_url[:8] + 'i.' + jpg_url[8:]  # Add i to imgur link if it's not there.
            image = fixed_url[20:]  # for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image]  # boolean for whether or not it failed

        elif url.find('redd.it') != -1:
            fixed_url = if_no_extension_add(url)
            image = fixed_url[18:]  # for imgur image, strip everything but id and .jpg
            return [True, fixed_url, image]  # boolean for whether or not it failed
        else:
            # If not from a supported url, return False
            return [False, url, 'Not supported:']

    except:
        return [False, 'Unidentified error during handleLink', url]


# Moves the downloaded image to wherever you would like to store it.
def move_image(image_name, image_directory):
    file_location = image_directory + image_name

    try:
        os.rename(image_name, file_location)

        return [True, file_location, 'Moved image to ' + file_location]
    except:
        os.remove(image_name)
        logging.warning(image_name + ' was deleted.')
        return [False, file_location, 'Failed to move file']


# Finds the image from the url and downloads it.
def get_image(url, image_location, image_directory):
    try:
        urllib.request.urlretrieve(url, image_location)
        logging.info(image_location + ' was downloaded.')
        image_moved = move_image(image_location, image_directory)

        if image_moved[0]:
            logging.info('{0} was moved to {1}'.format(image_location, image_directory))
            return [True, image_moved[1], 'Obtained and moved image to image folder']
        else:
            return [False, url, image_moved[2] + ' | ' + image_moved[1]]

    except:
        return [False, url, 'Failed to get image']


# download image for each submission
def download_all(submission, image_directory):
    link_result = handle_link(submission.url)
    # Make sure the handleLink didn't fail, the move onto getting the image
    if link_result[0]:
        get_image(link_result[1], link_result[2], image_directory)
        logging.info('{0} | {1}'.format(link_result[1], link_result[2]))
    else:
        logging.error('{0} | {1}'.format(link_result[1], link_result[2]))
