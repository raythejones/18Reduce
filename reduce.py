'''
Use list comprehension + reduce to do the following:
Find the frequency of a single word
Find the total frequency of a group of words
Find the most frequently occurring word
'''
import string

file = open("mobydic.txt", "r")
text = file.read()
file.close()
words = [word.strip(string.punctuation) for word in text.split()]

def freq(li, word):
    new_list = [1 for a in li if a == word]
    return reduce(lambda a, b: a + b, new_list)

print freq(words, "the")
print freq(words, "whale")
print freq(words, "white")

def group_freq(li, wordlist):
    new_list = [1 for a in li if a in wordlist]
    return reduce(lambda a, b: a + b, new_list)

print group_freq(words, ["the", "whale"])
print group_freq(words, ["white", "in"])
print group_freq(words, ["there", "omen"])

def most_freq(li):
    return reduce(lambda a, b: a if freq(li, a) > freq(li, b) and a != b else b, li)

print most_freq(words)
