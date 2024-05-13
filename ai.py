'''

ai.py - V1.2

A library of functions related to AI for use with AI-den.

This version is static - please do not modify this code. Instead modify the
original ai.py file found with the rest of the code for AI-den. To update this
file, replace it with a newer version of the ai.py file.

Author: Aiden Blishen Cuneo

'''

import openai
import tiktoken

openai.api_key = ''





def one_msg(msg, model='gpt-3.5-turbo'):
    return get_chat_response(
        [{'role': 'user', 'content': msg}],
        model=model)


def get_chat_response(msgs, model='gpt-3.5-turbo', retries=10, token_limit=4000):
    for _ in range(retries):
        try:
            res = openai.ChatCompletion.create(
                model=model,
                messages=msgs,
            )['choices'][0]
        except openai.error.InvalidRequestError:
            res = {
                'message': {
                    'content': '',
                },
                'finish_reason': 'length',
            }

        if res['finish_reason'] == 'stop':
            break

        if msgs:
            del msgs[0]

    return res['message']['content']


def get_code_response(msg):
    res = openai.Completion.create(
        engine='davinci-codex',
        prompt=f"'''Correct the following, or add to it if applicable'''\n{msg}",
        max_tokens=50,
    )

    code = res['choices'][0]['text']

    return f'[code response]\n{code}' if code else '<No response>'


def ask_question(question, model='gpt-3.5-turbo'):
    res = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'system', 'content': 'You are to respond to every question with'
                ' a yes or no answer, with no other words in your response.'},
            {'role': 'user', 'content': question + ' (respond with yes or no, even if not applicable)'},
        ],
    )

    reply = res['choices'][0]['message']['content']

    return 'yes' in reply.lower()


def parse_quote(text):
    if '"' not in text:
        return text

    return '"' + text.split('"')[1].strip() + '"'
