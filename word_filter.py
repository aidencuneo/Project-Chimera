import re
import string

bad = open('profanity_wordlist.txt').read().lower().split('\n')


def tok(text):
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text.split()


def is_bad(text):
    for w in tok(text.lower()):
        if w in bad:
            return True

    return False


result = is_bad(input('Enter text: '))
print('Sentence is ' + ('bad' if result else 'not bad'))
print("hi");
