# string_utils.py

def reverse_string(s):
    """Return the reverse of the input string."""
    return s[::-1]

def capitalize_string(s):
    """Return the input string with the first letter capitalized."""
    return s.capitalize()

def to_uppercase(s):
    """Return the input string in uppercase."""
    return s.upper()

def to_lowercase(s):
    """Return the input string in lowercase."""
    return s.lower()

def is_palindrome(s):
    """Return True if the input string is a palindrome, False otherwise."""
    cleaned_string = ''.join(c for c in s if c.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]
