import re
import string

bad = 'brotherfucker cyka blyat pigfuckerss Jesus wept in shit Christ cracker Christ bike sweet Jesus shitss Christ bike dickhead horseshit turd cocksucker pigfucker nigra goddamn holy shit dyke bastard bitch bloody bollocks brotherfucker bugger bullshit child-fucker Christ bike Christ cracker cock cocksucker crap cunt cyka blyat damn damn it dick dickhead dyke fatherfucker frigger fuck goddamn godsdamn hell holy shit horseshit in shit Jesus Christ Jesus fuck Jesus H. Christ Jesus Harold Christ Jesus, Marynd Joseph Jesus wept kike motherfucker nigga nigra pigfucker piss prick pussy shit shitss shite sisterfucker slut sof whore sof bitch spastic sweet Jesus turd twat wanker'.lower().split()


def tok(text):
    text = re.sub(rf'[{string.punctuation}]', '', text)
    return text.split()


def is_bad(text):
    for w in tok(text.lower()):
        if w in bad:
            return True

    return False


a = is_bad("I'm boat")
print('word is ' + ('bad' if a else 'not bad'))
