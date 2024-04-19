import re
import string
import util

bad = open('profanity_wordlist.txt').read().lower().split('\n')
chat_text = open('chat.txt', errors='ignore').read().lower().split('\n')


def tok(text):
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text.split()


def is_bad(text):
    for w in tok(text.lower()):
        if w in bad:
            return True

    return False


def checkBadMain(body):
    user_input = body['userInput']
    res = {'message': 'your input does not contain bad words'}

    if user_input == 'template':
        bad_word_list = [line for line in chat_text[:200] if is_bad(line)]
        res = {'bad_word_list': bad_word_list}

    elif is_bad(user_input):
        res = {'message': 'your input contains bad words'}

    return util.build_response(200, res)
