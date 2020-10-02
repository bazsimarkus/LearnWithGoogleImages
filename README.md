# LearnWithGoogleImages

**A simple Python program to help you memorise stuff using Google Image Search - in this case German words.**

## Setup

To be able to use this code, you need to enable Google Custom Search API, generate API key credentials and set up a project:

-   Visit  [https://console.developers.google.com](https://console.developers.google.com/)  and create a project.    
-   Visit  [https://console.developers.google.com/apis/library/customsearch.googleapis.com](https://console.developers.google.com/apis/library/customsearch.googleapis.com)  and enable "Custom Search API" for your project.
-   Visit  [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)  and generate API key credentials for your project.
-   Visit  [https://cse.google.com/cse/all](https://cse.google.com/cse/all)  and create a Custom Search Engine. Don't worry that it asks for a website to seach on, just type in www.anyurl.com to get past this screen, you can remove this setting later. After got past te screen, in the web form where you create/edit your custom search engine enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".
    
After doig this steps in your Google developers account and project you can get the API Key for your project and the CX for the Custom Search Engine. Replace them in the code, so that the program can use your own search engine.

To get the code working, you'll need to install the google-api-python-client:

    pip install google-api-python-client

After a successful installation, you can run the code and even apply some additional search criterias.
