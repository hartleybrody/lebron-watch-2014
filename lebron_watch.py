import re
import sys
import time
from datetime import datetime


import requests
from BeautifulSoup import BeautifulSoup

def main(twitter=False, website=False):
    if website:
        check_website()

    if twitter:
        check_twitter()


def check_website():

    delay = 5
    print "Checking website every {} seconds".format(delay)

    previous_response = None
    tries = 0

    while True:
        tries += 1

        r = requests.get("http://www.lebronjames.com/")
        if tries == 1:
            previous_response = r.text

        if r.text == previous_response:
            print "."
            time.sleep(delay)
            continue
        
        else:  # WEBSITE HAS CHANGED
            previous_response = r.text
            print "Website changed at {now}".format(now=datetime.now())
            print re.search(r"<title>([\w ]+)</title>", r.text).groups()[0]
            while True:
                print "\a\a"

def check_twitter():

    delay = 10
    print "Checking twitter every {} seconds".format(delay)

    previous_tweet = None
    tries = 0

    while True:
        tries += 1

        r = requests.get("https://twitter.com/KingJames")
        soup = BeautifulSoup(r.text)
        latest_tweet = soup.findAll("div", "ProfileTweet")[0]
        latest_tweet_text = latest_tweet.find("p", "ProfileTweet-text")

        if tries == 1:
            previous_tweet = latest_tweet_text

        if latest_tweet_text == previous_tweet:
            print "."
            time.sleep(delay)
            continue

        else:  # NEW TWEET
            previous_tweet = latest_tweet_text
            print "New Tweet found at {now}".format(now=datetime.now())
            print latest_tweet_text           
            while True:
                print "\a\a"



if __name__ == '__main__':

    if "-t" in sys.argv or "--twitter" in sys.argv:
        main(twitter=True)
    elif "-w" in sys.argv or "--website" in sys.argv:
        main(website=True)
    else:
        print "What would you like to check? Either his website (`-w` or `--website`) or his twitter (`-t` or `--twitter`)"
