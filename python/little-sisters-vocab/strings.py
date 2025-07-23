from typing import List

def add_prefix_un(word):
    """
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return f"un{word}"


def make_word_groups(vocab_words: List[str]) -> str:
    """ Add prefixes to word groups.
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    words = vocab_words[1:]
    return prefix + ' :: ' + ' :: '.join([prefix + w for w in words])


def remove_suffix_ness(word):
    """
  Removes the 'ness' suffix from a word, handling 'y' changes.

  Args:
    word: The word with the 'ness' suffix.
  Returns:
    The root word without the 'ness' suffix.
  """
    root_word = word[:-4]
    if root_word.endswith('i'):
        root_word = root_word[:-1] + 'y'
    return root_word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    if sentence[-1] == '.':
        sentence = sentence[:-1]
    words = sentence.split()
    return words[index] + 'en'