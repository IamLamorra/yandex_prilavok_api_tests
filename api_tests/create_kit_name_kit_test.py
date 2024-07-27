from api_tests import sender_stand_request, data

auth_token = sender_stand_request.get_new_user_token()


def get_kit_body(name):
    body = data.kit_body.copy()
    body["name"] = name
    return body


def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(get_kit_body("a"))


def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    )


def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(""))


def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(
        get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcD")
    )


def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert(get_kit_body("QWErty"))


def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert(get_kit_body("Мария"))


def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(get_kit_body('"№%@",'))


def test_create_kit_space_in_name_get_success_response():
    positive_assert(get_kit_body("Человек и КО"))


def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(get_kit_body("123"))


def test_create_no_name_get_error_response():
    negative_assert_code_400(dict())


def test_create_kit_number_type_in_name_get_error_response():
    negative_assert_code_400(get_kit_body(123))
