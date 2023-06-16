def is_palindrome_iterative(word):
    if not word:
        return False
    return word == word[::-1]


# solução tirada de
# www.w3schools.com/python/python_howto_reverse_string.asp
