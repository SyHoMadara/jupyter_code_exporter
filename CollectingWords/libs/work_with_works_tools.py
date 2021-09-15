"""
tools for working on persian file
"""
from beartype import beartype

PERSIAN_ALPHABET = ["ؠ", "ء", "آ", "أ", "ؤ", "إ", "ئ", "ا", "ب", "ة", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س",
                    "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ػ", "ؼ", "ؽ", "ؾ", "ؿ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و",
                    "ى", "ي", "ٲ", "ٳ", "ٵ", "ٶ", "ٷ", "ٸ", "ٹ", "ٺ", "ٻ", "ټ", "ٽ", "پ", "ٿ", "ڀ", "ځ", "ڂ", "ڃ", "ڄ",
                    "څ", "چ", "ڇ", "ڈ", "ډ", "ڊ", "ڋ", "ڌ", "ڍ", "ڎ", "ڏ", "ڐ", "ڑ", "ڒ", "ړ", "ڔ", "ڕ", "ږ", "ڗ", "ژ",
                    "ڙ", "ښ", "ڛ", "ڜ", "ڝ", "ڞ", "ڟ", "ڠ", "ڡ", "ڢ", "ڣ", "ڤ", "ڥ", "ڦ", "ڧ", "ڨ", "ک", "ڪ", "ګ", "ڬ",
                    "ڭ", "ڮ", "گ", "ڰ", "ڱ", "ڲ", "ڳ", "ڴ", "ڵ", "ڶ", "ڷ", "ڸ", "ڹ", "ں", "ڻ", "ڼ", "ڽ", "ھ", "ڿ", "ۀ",
                    "ہ", "ۂ", "ۃ", "ۄ", "ۅ", "ۆ", "ۇ", "ۈ", "ۉ", "ۊ", "ۋ", "ی", "ۍ", "ێ", "ۏ", "ې", "ۑ"]
ENGLISH_ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


@beartype
def is_number(string: str):
    try:
        int(string)
        return True
    except ValueError:
        return False


@beartype
def is_persian_word(word: str) -> bool:
    valid = True
    # has valid persian letter
    for letter in word:
        if (letter < PERSIAN_ALPHABET[0]
                or letter > PERSIAN_ALPHABET[-1]):
            valid = False
            return valid

    return valid


@beartype
def is_valid(string: str, valid_chars: list):
    """
    A function for validating a string
    :param string:
    :param valid_chars: list of Requirement instance that get letter and return boolean value
    :return:
    """
    # validate requirements that be valid values
    for valid_char in valid_chars:
        if not isinstance(valid_char, str) or not len(valid_char) == 1:
            raise ValueError("requirements contain non character instance values(be string with length 1)")

    for letter in string:
        if letter not in valid_chars:
            return False

    return True
