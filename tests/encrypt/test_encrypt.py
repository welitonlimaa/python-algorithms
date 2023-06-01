# import pytest

from challenges.challenge_encrypt_message import encrypt_message


# @pytest.mark.parametrize(
#     "message, key, expected",
#     [
#         ("aloalo", 3, "ola_ola"),
#         ("aloalo", "B", "tipo inválido para key"),
#         (6594, 3, "tipo inválido para message"),
#         ("olaola", 9, "ola_ola"),
#     ],
# )
def test_encrypt_message():
    assert encrypt_message("aloalo", 3) == "ola_ola"
    assert encrypt_message("aloalo", 10) == "olaola"
    try:
        encrypt_message("aloalo", "B")
    except TypeError as e:
        print("error", str(e) == "tipo inválido para key")
        assert str(e) == "tipo inválido para key"

# def test_encrypt_message():
#     assert encrypt_message("aloalo", 3) == "nnaja"
