from __future__ import annotations
from string import ascii_letters


def encrypt(plaintext: str, key: int, alphabet: str | None = None) -> str:
    result = ""
    # 选择字母表
    alphabet = alphabet or ascii_letters

    for character in plaintext:
        try:
            index = alphabet.index(character)
        except ValueError:
            pass
        else:
            # 3 % 26 -> 3, -3 % 26 -> 23
            index = (index + key) % len(alphabet)
            character = alphabet[index]

        result += character

    return result


def decrypt(ciphertext: str, key: int, alphabet: str | None = None) -> str:
    key *= -1
    return encrypt(ciphertext, key, alphabet)


def brute_force(ciphertext: str, key: int, alphabet: str | None = None) -> dict[int, str]:
    data = {}
    alphabet = alphabet or ascii_letters
    for key in range(1, len(alphabet) + 1):
        data[key] = decrypt(ciphertext, key, alphabet)

    return data
