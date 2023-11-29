from pytube import YouTube
from flask import Flask, render_template, request
import os
import instaloader
import urllib.parse
import shutil

app = Flask(__name__)
@app.route('/', methods=['GET'])
def HomePage():
    return render_template('HomePage.html')

@app.route("/input", methods=['POST'])
def get_options():
    selected_option = request.form['select_options']
    if selected_option == 'Youtube':
        return render_template("Youtube.html")
    elif selected_option == 'Instagram':
        return render_template("Instagram.html")
    elif selected_option == 'X':
        return render_template("X.html")
    elif selected_option == 'nothing':
        return render_template("nothing.html")
    
@app.route("/input/youtube", methods=['POST'])
def YoutubeDownload():
    video_url= request.form['URL']
    def download_vid(url):
        try:
            video=YouTube(url)
            stream=video.streams.get_highest_resolution()
            stream.download()
            return True
        except Exception as e:
            print(f"Error downloading video: {e}")
            return False
    
    Success = download_vid(video_url)
    if Success:
        folder_name = 'Youtube_Downloads'
        abs_folder_path = os.path.abspath(folder_name)
        os.makedirs(abs_folder_path, exist_ok=True)
        for filename in os.listdir('.'):
            if filename.endswith('.mp4'):
                abs_file_path = os.path.abspath(filename)
                shutil.move(abs_file_path, os.path.join(abs_folder_path, filename))
        return render_template("SuccessPage.html")
    else:
        return render_template("ErrorPage.html")

@app.route("/input/Instagram", methods=['POST'])
def InstagramDownload():
    I = instaloader.instaloader()
    def username_from_url(url):
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc == 'www.instagram.com' and parsed.path != '':
            return parsed.path.split('/')[1]
        return None
    
    url = request.form['URL']
    username = username_from_url(url)
    def profile_download(name):
        try:
            I.download_profile(name, profile_pic=True)
        except instaloader.exceptions.InstaloaderException as e:
            print(f"Error downloading Instagram profile: {e}")
            return render_template("ErrorPage.html")

        folder_name = name
        abs_folder_path = os.path.abspath(folder_name)
        os.makedirs(abs_folder_path, exist_ok=True)

        for filename in os.listdir('.'):
            if not filename.startswith(name):
                continue
            if filename.endswith('.jpg') or filename.endswith('.mp4'):
                abs_file_path = os.path.abspath(filename)
                shutil.move(abs_file_path, os.path.join(abs_folder_path, filename))

    profile_download(username)
    return render_template("SuccessPage.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
