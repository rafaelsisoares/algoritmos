def is_palindrome_recursive(word, low_index, high_index):
    print(low_index, high_index)
    if len(word) == 0 or word[low_index] != word[high_index]:
        return False
    if low_index != high_index and high_index > 0:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
