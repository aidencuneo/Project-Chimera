import json

def build_response(status_code, message=None):
    response = {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Adjust CORS policy as needed
        }
    }
    if message:
        response['body'] = json.dumps({'message': message})
    return response