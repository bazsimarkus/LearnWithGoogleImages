# LearnWithGoogleImages

**A simple, small Python program to help you memorise stuff using Google Image Search - in this case German words.**

## Screenshot

> **Note:**  The screenshot was taken on a Windows PC.

![LWGI screenshot](https://raw.githubusercontent.com/bazsimarkus/LearnWithGoogleImages/master/LWGI_screenshot.png)

## How it works

The software reads a customizable CSV table, which in the first column contains the words we'd like to learn, with their translation being in the second column (in the same row).
After that, it chooses a random word, and using the Google Custom Search API it does a Google Image Search, then shows the most relevant image found, without showing the word, so you can test whether you know the word or not.
If you don't know the word, you can show it by clicking on the "Show Word" button. If you would like to know the translation for the word (which is in this case, the Hungarian form), just click the "Show Translation" button.
When clicking the "New Image" button, the program clears the previous words and the image, chooses a new random word from the word list, and does the same as with the previous image.

## Setup

To be able to use this code, you need to enable Google Custom Search API, generate API key credentials and set up a project:

-   Visit  [https://console.developers.google.com](https://console.developers.google.com/)  and create a project.    
-   Visit  [https://console.developers.google.com/apis/library/customsearch.googleapis.com](https://console.developers.google.com/apis/library/customsearch.googleapis.com)  and enable "Custom Search API" for your project.
-   Visit  [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)  and generate API key credentials for your project.
-   Visit  [https://cse.google.com/cse/all](https://cse.google.com/cse/all)  and create a Custom Search Engine. Don't worry that it asks for a website to seach on, just type in www.anyurl.com to get past this screen, you can remove this setting later. After got past te screen, in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".
    
After doing this steps in your Google developers account and project you can get the API Key for your project and the CX for the Custom Search Engine. Replace them in the code of the googleApiCredentials.py file, so that the program can use your own search engine.

    my_api_key = "YOUR_API_KEY"
    my_cse_id = "YOUR_CSE_ID"

    
To get the code working, you'll need to install the google-api-python-client:

    pip install google-api-python-client

After a successful installation, you can run the code and even apply some additional search criterias. Unfortunately the free Google API Key is limited to 100 searches/day, but it's enough to play a bit around with the software.
