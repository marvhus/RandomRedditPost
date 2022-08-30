#!/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# Return a image, and subreddit for a random post on a given subreddit.
# Default subreddit (sr) = r/memes
def get_meme(sr = "memes"):
    # Request data
    url = f"https://meme-api.herokuapp.com/gimme/{sr}"
    response = json.loads(requests.get(url).text)
    # Extract data
    link = response["postLink"]
    title = response["title"]
    meme_large = response["preview"][-2]
    author = response["author"]
    ups = response["ups"]
    subreddit = response["subreddit"]

    # Return data
    return meme_large, subreddit, title, link, author, ups

@app.route("/<name>")
def subreddit(name):
    meme_pic, subreddit, title, link, author, ups = get_meme(name)
    return render_template(
        "index.html", 
        meme_pic=meme_pic, 
        subreddit=subreddit, 
        title=title, 
        link=link, 
        author=author, 
        ups=ups
    )

@app.route("/")
def index():
    return subreddit("memes")

app.run(host="0.0.0.0", port="5000")
