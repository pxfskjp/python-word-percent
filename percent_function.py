import re
def word_percent(word, file_name):
    f = open(file_name, "r")
    origin_text = f.read()
    text = re.sub('[^A-Za-z0-9]+', ' ', origin_text)
    wordlist = text.split()

    totalcount = len(wordlist)
    wordfreq = []
    wordfreqs = []
    for w in wordlist:
        word_frequency = (wordlist.count(w)/totalcount)*100
        wordfreqs.append(wordlist.count(w))
        wordfreq.append(word_frequency)

    print("text\n" + origin_text +"\n")
    print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

word_percent("was", "sample_text.txt")