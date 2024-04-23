import util
from AnalyseSentiment.AnalyseSentiment import AnalyseSentiment

analyser = AnalyseSentiment()


def analyse_sentiment(body):
    user_input = body['userInput']

    data = analyser.Analyse(user_input)
    res = {'result': data}

    return util.build_response(200, res)


r = analyse_sentiment({'userInput': input('\nType something: ')})
print(r)
