import json
import word_filter
import util

def lambda_handler(event, context):
    print('Request Event: ', event)
    response = None
    # http_method = event['httpMethod']
    http_method = event.get('httpMethod')
    if http_method is None:
        # Check if requestContext is present
        if 'requestContext' in event and 'http' in event['requestContext']:
            http_method = event['requestContext']['http']['method']
        else:
            # If requestContext is not present or http method is not found, return an error response
            return util.build_response(400, "Bad Request: HTTP method not specified")

    path = event['path']
    body = json.loads(event.get('body', '{}'))

    if http_method == 'GET' and path == '/health':
        response = util.build_response(200, event)
    elif http_method == 'POST' and path == '/check-bad-words':
        response = word_filter.checkBadMain(body)
    else:
        response = util.build_response(404, "Not Found")
    return response