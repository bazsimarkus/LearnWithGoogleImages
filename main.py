import pprint
import random

from googleImageSearch import *
from readfile import *

def getNewWordNumber():
    return random.randrange(0, len(wordList)-1)

def getNewImage():
    word_to_search = wordList[getNewWordNumber()]
    print(word_to_search)
    results = google_search(word_to_search, my_api_key, my_cse_id, num=3)
    for result in results:
        pprint.pprint(result)

def main():
    readWordListFromFile()
    getNewImage()

if __name__ == '__main__':
  main()
