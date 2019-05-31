#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def print_words(content):
    # print(content)
    words = content.lower().split()
    words_count = {}
    for word in words:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

    # return sorted(words_count.keys())
    for word in sorted(words_count):
	    print(word + ': ' + str(words_count[word]))

def print_top(content):
    words_count = {}
    # print(content)
    words = content.lower().split()
    for word in words:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

    def keyfunction(k):
        return words_count[k]

    for key in sorted(words_count, key=keyfunction, reverse=True)[:20]:
        print ("%s: %i" % (key, words_count[key]))


    # top_twenty = sorted(words_count, key=lambda tup: tup[1], reverse=True)
    # print(top_twenty)
  

    # return words_count


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def main():
    print(sys.argv)
    if len(sys.argv) < 1:
        print('usage: python wordcount.py file {--count | --topcount}')
        sys.exit(1)
        return

    filename = sys.argv[1]
    option = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

    with open(filename, "r") as filename1:
        file_contents = filename1.read()
        # print(filename_contents)
        print(print_top(file_contents))


if __name__ == '__main__':
    main()
