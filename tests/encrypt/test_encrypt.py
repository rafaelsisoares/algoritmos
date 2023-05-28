import pytest
from challenges.challenge_encrypt_message import encrypt_message

THREE = 3
FOUR = 4


def test_encrypt_message():
    message = 'teste'
    encrypted_message_odd = encrypt_message(message, THREE)
    encrypted_message_even = encrypt_message(message, FOUR)
    inverted_message = encrypt_message(message, -2)
    assert encrypted_message_odd == 'set_et'
    assert encrypted_message_even == 'e_tset'
    assert inverted_message == 'etset'

    with pytest.raises(TypeError):
        encrypt_message(THREE, message)
