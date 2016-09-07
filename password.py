#!/usr/bin/python

import argparse
import random
import math

# extract words from words.txt
# assumes each word is on its own line, no quotes/spaces/etc.
def words_from_file():
  f = open('words.txt', 'r')
  lines = f.readlines()
  f.close()

  # remove \n
  words = [line[:-1] for line in lines]
  return words

# extracts a random word from a list of words
def random_word(words):
  # SystemRandom relies on /dev/urandom
  r = random.SystemRandom()
  return r.choice(words)

# extracts n random words from a list of words
def random_words(words, n):
  chosen = []
  for i in range(n):
    new_word = random_word(words)
    chosen.append(new_word)
  return chosen

def entropy_per_word(words):
  n = len(words)
  return math.log(n, 2)

def args():
  parser = argparse.ArgumentParser(description='Randomly generate a password from a list of words')
  parser.add_argument('-n', '--num', help='Number of words to generate. Defaults to 5.', type=int, default=5)
  args = parser.parse_args()
  return args

def run(num):
  words = words_from_file()
  chosen = random_words(words, num)
  entropy = entropy_per_word(words)
  total_entropy = entropy*num

  print "chosen words:"
  for word in chosen:
    print "  " + word
  print "entropy per word: " + str(entropy)
  print "total entropy: " + str(total_entropy)

if __name__ == '__main__':
  args = args()
  n = args.num
  run(n)
