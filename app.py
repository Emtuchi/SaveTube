from pytube import YouTube
from flask import Flask, render_template, request
from pywebcopy import save_webpage
import gdown
import os
import instaloader
import urllib.parse
import shutil
from test import is_valid_url, is_valid_username

app = Flask(__name__)
@app.route('/', methods=['GET'])
def HomePage():
    # renders the home page
    return render_template('HomePage.html')

@app.route('/HomePage/about/LandingPage')
def LandingPage():
    # renders the landing page
    return render_template('LandingPage.html')

@app.route("/input", methods=['POST'])
def get_options():
    ''' handles redirections to desired webpage from
        selected options from home page'''
    
    selected_option = request.form['select_options']
    if selected_option == 'Youtube':
        return render_template("Youtube.html")
    elif selected_option == 'Instagram':
        return render_template("Instagram.html")
    elif selected_option == 'WebPage':
        return render_template("SourceCode.html")
    elif selected_option == 'Google_Drive':
        return render_template("GoogleDrive.html")
    elif selected_option == 'nothing':
        return render_template("LandingPage.html")
    
@app.route("/input/youtube", methods=['POST'])
def YoutubeDownload():
    # Handles youtube video downloads
    url= request.form['URL']
    if is_valid_url(url):
        video=YouTube(url)
        stream=video.streams.get_highest_resolution()
        stream.download()
        folder_name = 'Youtube_Downloads'
        abs_folder_path = os.path.abspath(folder_name)
        os.makedirs(abs_folder_path, exist_ok=True)
        for filename in os.listdir('.'):
            if filename.endswith('.mp4'):
                abs_file_path = os.path.abspath(filename)
                shutil.move(abs_file_path, os.path.join(abs_folder_path, filename))
        return render_template("SuccessPage.html")
    else:
        return render_template("ErrorPage.html", Error="not a valid url")

@app.route("/input/Instagram", methods=['POST'])
def InstagramDownload():
    # handles instagram downloads
    url = request.form['URL']
    username = request.form['username']
    if is_valid_url(url) and is_valid_username(username):
        Ig = instaloader.Instaloader()
        post_shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(Ig.context, post_shortcode)
        abs_folder_path = os.path.abspath(username)
        os.makedirs(abs_folder_path, exist_ok=True)
        Ig.download_post(post, abs_folder_path)
        return render_template("SuccessPage.html")
    else:
        return render_template("ErrorPage.html", Error="incorrect username or url")
    

@app.route("/input/SourceCode", methods=['POST'])
def Source_download():
    # handles downloading source code of a webpage
    url = request.form['URL']
    if is_valid_url(url):
        current_directory = os.getcwd()
        
        name = urllib.parse.urlparse(url)
        domain = name.netloc.split('.')
        folder_name = domain[1] if len(domain) > 1 else domain[0]
        
        save_webpage(
            url=url,
            project_folder=current_directory,
            project_name=folder_name,
            bypass_robots=True,
            debug=True,
            open_in_browser=True,
            delay=None,
            threaded=False,
            )
        return render_template("SuccessPage.html")
    else:
        return render_template("ErrorPage.html", Error="not a valid url")
    
@app.route("/input/GdriveDownload", methods=['POST'])
def gdrive_download():
    # handles google drive file or folder downloads
    option = request.form['options']
    url = request.form['URL']

    if option == 'download_file' and is_valid_url(url):
        file_id = url.split('/')[-2]
        new_url = f'https://drive.google.com/uc?/export=download&id={file_id}'
        gdown.download(new_url)
        return render_template("SuccessPage.html")
    elif option == 'download_folder' and is_valid_url(url):
        if url.endswith('?usp=sharing'):
            url = url[:-len('?usp=sharing')]
            gdown.download_folder(url)
            return render_template("SuccessPage.html")
    else:
        return render_template("ErrorPage.html", Error="not a valid url")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
