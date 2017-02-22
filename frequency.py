""" Analyzes the word frequencies in "The Metamorphosis" by Franz Kafka
 downloaded from Project Gutenberg.

 Author: Onur, the Incompetent

"""

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('Copyright (C) 2002 David Wyllie.') == -1:
        curr_line += 1
    lines = lines[curr_line+1:1995]

    for i in range(0, len(lines)):
        lines[i] = lines[i][0:len(lines[i])-1]
    raw_list = " ".join(lines)

    punc_table = " "*len(string.punctuation)
    punc_removed = raw_list.translate(str.maketrans(string.punctuation, punc_table))
    lowercase = punc_removed.lower()
    final_list = lowercase.split()
    return final_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """

    histogram = dict()
    for word in word_list:
        histogram[word] = histogram.get(word, 0)+1

    ordered_by_frequency = sorted(histogram.items(), key=lambda x: x[1], reverse=True)
    return(ordered_by_frequency[:100])


if __name__ == "__main__":
    word_list = get_word_list('metamorphosis.txt')
    get_top_n_words(word_list, 100)
    # print(get_top_n_words(word_list, 100))
