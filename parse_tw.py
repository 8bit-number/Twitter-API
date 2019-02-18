# gets needed data from user and according to that

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def intro():
    """
    tells user how to use this program
    :return: None
    """
    print(
    """
    welcome! 
    here you can see some basic information about people you follow on twitter.
    to use this application, just follow the instructions given right next to
    each prompt. have a nice time using it ;)
    """)

def number_of_friends():
    """
    asks user to enter how many people do they want to see in the table
    :return: the number of friends
    """
    while 1:
        num_fr = input("enter how many friends you\'d like to see: ")
        if num_fr.isdigit() or not num_fr:
            break
        else:
            print("enter a valid number")
    return num_fr

def user_name():
    """
    asks to enter the username
    :return: the username
    """
    while 1:
        username = input("enter username, please: ")
        if not len(username) == 0:
            return username



def get_users(acct, num):
    """
    gets username and returns the list of json items
    :return: json filename (str)
    """

    users = []
    try:

        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct.lower(), 'count': num})

        connection = urllib.request.urlopen(url, context=ctx)
        # print(connection)
        data = connection.read().decode()
        js = json.loads(data)
        users = js.get("users") or []
        return users


    except urllib.error.HTTPError:
        print("enter a valid username: ")
        return users

if __name__ == "__main__":
    intro()
    num = number_of_friends()
    acct = user_name()
    print(get_users(acct, num))
