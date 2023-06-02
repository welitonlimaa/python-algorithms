def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    inverted_word = "".join(reversed(word))
    return word == inverted_word


print(is_palindrome_iterative("amor"))
