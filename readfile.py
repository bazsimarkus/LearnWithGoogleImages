import csv

wordList = []

def readWordListFromFile():
    with open("wordlist.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            wordList.append(row)