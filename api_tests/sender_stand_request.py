import requests

from api_tests import configuration, data


def get_new_user_token():
    create_user_response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers
    )
    auth_token = create_user_response.json()["authToken"]
    return auth_token


def post_new_client_kit(body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=body,
                         headers=headers)
