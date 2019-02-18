# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings
import json


def oauth():
    with open("api_keys.json") as jf:

        return json.load(jf)

# print(oauth())
