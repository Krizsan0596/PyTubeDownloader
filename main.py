
from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download/", methods = ["POST"])
def download():
    yt_url = request.form["yturl"]
    yt_download(yt_url)
    return yt_url

def yt_download(link):
    print("Youtube Downloader")
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Video length: ", yt.length, "seconds")
    ys = yt.streams.get_highest_resolution()
    print("Processing...")
    ys.download()
    print("Video downloaded")

if __name__ == "__main__":
    app.run()