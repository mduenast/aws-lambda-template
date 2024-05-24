import json


def lambda_handler(event, context):
    """
    :param event: JSON object containing the event details passed to the Lambda function.
                  It can contain any arbitrary data, but it is commonly used to pass input parameters.
                  The event object may have a 'name' field which will be used to construct the response.
    :param context: AWS Lambda runtime information and methods object that contains information about
                    the execution environment and methods to manage the function's lifecycle.
    :return: JSON object containing the HTTP status code and body of the response to be returned from
             the Lambda function. The body contains a JSON representation of the response object.
    """
    # print the event details to the CloudWatch log
    print('Event Received: ' + json.dumps(event, indent=2))

    # extract the 'name' field from the event object, use "World" as a default value
    name = event.get('name', 'World')

    # construct the body of the response object
    response = {
        "greeting": "Hello, " + name + "!"
    }

    # Create the response to return from the Lambda function
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }