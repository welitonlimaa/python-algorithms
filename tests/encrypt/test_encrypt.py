import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("aloalo", 3) == "ola_ola"
    assert encrypt_message("aloalo", 4) == "ol_aola"
    assert encrypt_message("aloalo", 10) == "olaola"

    with pytest.raises(TypeError):
        encrypt_message("aloalo", "B")
    with pytest.raises(TypeError):
        encrypt_message(12354, 3)
