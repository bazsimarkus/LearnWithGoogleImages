wordList = []

def readWordListFromFile():
    with open("wordlist.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            wordList.append(stripped_line)
