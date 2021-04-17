from dynamodb.dynamodb_question_accessor import QuestionDDBAccessor
import json


def handler(event, context):
    print(f"event: {event}")

    if event['httpMethod'] == 'GET' and event['path'] == '/v1/questions':
        return handle_get_all_questions()

    return return_get_response(200, {
        'Hello': '1',
        'From': '2',
        'Lambda': '3'
    })


def return_get_response(status_code: int, payload: dict):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(payload)
    }


def handle_get_all_questions():
    questions = QuestionDDBAccessor.get_all_items()
    print(f"Got questions: {questions}")
    return return_get_response(200, questions)
