"""
tools for making files clean, extracting persian word, remove other characters not needed.
"""
from typing import Optional

HALF_SPACE_UTF8_CODE = b'\xe2\x80\x8c'
VIRGOL_UTF8_CODE = b'\xd8\x8c'
HAMZE_UTF8_CODE = b'\xd8\xa1'
A_UTF8_CODE = b'\xd8\xa2'  # آ
UNKNOWN_CHAR_MARK = b'\xc2\xa7'

UTF8 = "utf-8"


def is_number(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_valid(letter: str) -> bool:
    valid = True
    # has valid persian letter
    for let in letter:
        if (let.encode(UTF8) < "آ".encode(UTF8)
                or let.encode(UTF8) > "ی".encode(UTF8)):
            valid = False
            return valid

    return valid


def make_valid_letter(letter: str) -> Optional[str]:
    """
    This function get a letter than make it valid by following condition
        if letter == "آ" than return "ا"
        if letter be virgole,
                     hamze,
                     half space,
                     English(every character with ASCII code between 0 and 127 except space),
                     number,
                            than return None.
        else it return that letter
    :param letter:
    """

    letter_code = letter.encode(UTF8)
    if (letter_code == VIRGOL_UTF8_CODE
        or letter_code == HAMZE_UTF8_CODE
        or letter_code == UNKNOWN_CHAR_MARK
        or letter_code == HALF_SPACE_UTF8_CODE
        or (127 >= ord(letter) >= 0 and letter != ' ')
        or is_number(letter)) \
        and letter_code != A_UTF8_CODE:
            return None
    elif letter_code == A_UTF8_CODE:
        return 'ا'
    else:
        return letter