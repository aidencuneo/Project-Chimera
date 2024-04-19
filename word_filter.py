import re
import string
import util

bad = open('profanity_wordlist.txt').read().lower().split('\n')


def tok(text):
    text = re.sub(f'[{string.punctuation}]', '', text)
    return text.split()


def is_bad(text):
    for w in tok(text.lower()):
        if w in bad:
            return True
    return False


# result = is_bad(input('Enter text: '))
# print('Sentence is ' + ('bad' if result else 'not bad'))

def checkBadMain(userInput):
    # user_input = str(userInput)
    user_input = userInput['userInput']
    try:
        if user_input == 'template':
            good_word_list = []
            chat_text_opener = open('chat.txt', errors='ignore').read().lower().split('\n')
            for text in chat_text_opener[:200]:
                if is_bad(text):
                    # print('not bad:', text, end='\n\n')
                    good_word_list.append(text)

            response_body = {"bad_word_list": good_word_list}
            return util.build_response(200, response_body)
        else:
            for word in user_input.split():
                if is_bad(word):
                    return util.build_response(200, {
                        "message": "your input contains bad words"
                    })
        
    except KeyError as e:
        missing_keys = str(e).strip("''")
        error_message = f"Bad request - Missing '{missing_keys}' in the event"
        print(error_message)
        return util.build_response(400, {"message": error_message})