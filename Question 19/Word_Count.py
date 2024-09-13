# word_count.py

from collections import Counter

def count_words(file_name):
    with open(file_name, 'r') as file:
        text = file.read().lower()
    words = text.split()
    word_count = Counter(words)
    
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

count_words('paragraph.txt')
