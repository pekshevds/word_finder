def delete_some_simbols_from_word(word):
    """
    cleaning the word from unnecessary characters
    """

    return "".join(ch for ch in word if ch.isalpha() or ch.isdigit()).lower()


def split_some_text_into_words(text):
    """
    split some text into words
    """
    return text.split(' ')


def get_cleared_words(text):
    """
    split text into words and cleare them
    """

    dirty_words = split_some_text_into_words(text)
    return list(map(delete_some_simbols_from_word, dirty_words))