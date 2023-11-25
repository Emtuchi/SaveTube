from pytube import YouTube
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def HomePage():
    return render_template('HomePage.html')

@app.route("/downloads", methods=['POST'])
def downloads():
    if request.method == "POST":
        result= request.form
        video_url= request.form['URL']
        def download_vid(url):
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()
            stream.download()
        download_vid(video_url)
        return render_template("NextPage.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
