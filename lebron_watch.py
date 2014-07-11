import requests
from BeautifulSoup import BeautifulSoup

import time
from datetime import datetime
import re

def main():
    check_website()
    # check_twitter()


def check_website():

    previous_response = None
    tries = 0

    while True:
        tries += 1

        r = requests.get("http://www.lebronjames.com/")
        if tries == 1:
            previous_response = r.text

        print re.search(r"<title>([\w ]+)</title>", r.text).groups()[0]

        if r.text == previous_response:
            time.sleep(3)  # wait before we try again
            continue
        else:
            previous_response = r.text
            print "Website changed at {now}".format(now=datetime.now())
            while True:
                print "\a\a"

def check_twitter():

    previous_tweet = None
    tries = 0

    while True:
        tries += 1

        r = requests.get("https://twitter.com/KingJames")
        soup = BeautifulSoup(r.text)
        latest_tweet = soup.findAll("div", "ProfileTweet")[0]
        latest_tweet_text = latest_tweet.find("p", "ProfileTweet-text")

        print latest_tweet_text

        if tries == 1:
            previous_tweet = latest_tweet_text

        if latest_tweet_text == previous_tweet:
            time.sleep(10)
            continue

        else:
            previous_tweet = latest_tweet_text
            print "New Tweet found at {now}".format(now=datetime.now())            
            while True:
                print "\a\a"



if __name__ == '__main__':
    main()