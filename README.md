# YTViewer

**YTViewer** is simple YouTube views bot

## Prerequisites

### Windows

Install **Google Chrome Browser**: https://www.google.com/chrome/

Download **ChromeDriver** and move the executable to folder in your **PATH**: http://chromedriver.chromium.org/downloads

Or

Install **Mozilla Firefox Browser**: https://www.mozilla.org/en-US/firefox/new/

Download **geckodriver**, unzip and move the executable to folder in your **PATH**: https://github.com/mozilla/geckodriver/releases

## Installation

### Windows

Install Python: https://www.python.org/downloads/

```
git clone "https://github.com/DeBos99/ytviewer.git"
cd ytviewer
install.bat
cd ..
```

### Linux & MacOS

```
git clone "https://github.com/DeBos99/ytviewer.git"
cd ytviewer
sudo chmod +x install.sh
sudo ./install.sh
cd ..
```

## Usage

Show help:

`$ python main.py --help`

Set url of the video to **URL**:

`$ python main.py --url URL`

Set number of the threads to **T** (default: 15):

`$ python main.py --url URL --threads T`

Set the duration of video in seconds to **S** (default: 300 seconds (5 minutes)):

`$ python main.py --url URL --duration S`

Set the path of proxies list to **PATH** (default: proxies loaded from web):

`$ python main.py --url URL --proxies PATH`

Set the user agent for the driver to **AGENT** (default: randomly generated user agent):

`$ python main.py --url URL --user-agent AGENT`

Set the path of the list of the user agents for the driver to **PATH**:

`$ python main.py --url URL --user-agents PATH`

Set the driver for the bot to chrome:

`$ python main.py --url URL --driver chrome`

Set the driver for the bot to firefox:

`$ python main.py --url URL --driver firefox`

## TODO

* Add autamatic video duration.
* Add support for multiple urls.

## Authors

* **Michał Wróblewski** - Main Developer - [DeBos99](https://github.com/DeBos99)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
