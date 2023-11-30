# SaveTube


SaveTube is an advanced Python-based web application designed to simplify downloading content from YouTube and Instagram. This user-friendly application allows seamless retrieval of videos from YouTube and profiles from Instagram.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Installation
To run SaveTube locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/SaveTube.git
    cd SaveTube
    ```

2. Install the required dependencies:

    SaveTube utilizes the following libraries:
    - Flask: A micro web framework for Python.
    - pytube: A library for downloading YouTube videos.
    - instaloader: A tool to download pictures (or videos) along with their captions and other metadata from Instagram.

    You can install these dependencies via pip:

    ```
    pip3 install Flask pytube instaloader
    ```

3. Run the application:

    ```
    python3 app.py
    ```

4. Access the application by navigating to [http://localhost:5000](http://localhost:5000) in your web browser.

## Features
- **YouTube Download**
  - Select the "YouTube" option from the dropdown menu on the homepage.
  - Input the URL of the YouTube video you want to download.
  - Click the "Download video" button to retrieve the highest resolution version of the video.

- **Instagram Download**
  - Choose the "Instagram" option from the dropdown menu on the homepage.
  - Enter the URL of the Instagram profile you wish to download.
  - Click the "Download Profile" button to save the profile's pictures and videos.

- **Additional Options**
  - The application also supports other functionalities denoted as "X" and "nothing" options in the dropdown menu.

## Usage
1. Open your web browser and go to [http://localhost:5000](http://localhost:5000).
2. Select your desired option from the dropdown menu.
3. Provide the necessary URL as prompted.
4. Click the corresponding download button to retrieve the content.

## Libraries Used
- **Flask**: A micro web framework for Python used for building web applications.
- **pytube**: A library to easily download YouTube videos.
- **instaloader**: A tool for downloading pictures (or videos) along with their captions and other metadata from Instagram.

## Contributing
We welcome contributions! If you'd like to improve this project, please:
1. Fork the repository.
2. Create your branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Support
If you encounter any issues or have suggestions for improvements, feel free to open an issue.

## License
This project is licensed under the MIT License.

