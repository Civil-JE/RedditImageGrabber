'''
Author: Josh Eastman
Updated: 02/16/18
Version 1.0.0
Description: Instance file for RedditImageGrabber. Creates the instanced needed for the script to crawl through Reddit. 
'''

import praw
import tweepy

class RedditInstance:
    #Information is read from Credentials.txt
    client_id = "" 
    client_secret = ""
    user_agent = ""  
#    username = ""
#    password = ""
    
    reddit_instance = None

    def __init__(self):
        #credentialsFile = "credentials/Credentials.txt" #Prod
        credentials_file = "credentials/testCredentials.txt" #Test
        openedFile = open(credentials_file,"r")
        credentials = openedFile.readlines()

        #Had to add .strip to remove invisible whitespaces/leading characters
        self.client_id = credentials[0].strip()
        self.client_secret = credentials[1].strip()
        self.user_agent = credentials[2].strip()
#        self.username = credentials[3].strip()
#        self.password = credentials[4].strip()


        #Don't need to provide user details due to only needing a Read Only instance.
        self.reddit_instance = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret,
                             user_agent=self.user_agent)  
