import string

"""
This program recieves a text and returns the most frequent letter in
it.

Ex: 
most_frequent_letter("abacaxi") // return 'a'
"""

def most_frequent_letter(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
