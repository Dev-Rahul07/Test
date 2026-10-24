"""Debugging practice: this palindrome check has an intentional bug."""


def is_palindrome(text):
    # Bug: comparison is case-sensitive and includes spaces and punctuation.
    return text == text[::-1]


if __name__ == "__main__":
    phrase = "A man, a plan, a canal: Panama"
    print("Is palindrome:", is_palindrome(phrase))  # Incorrectly prints False
