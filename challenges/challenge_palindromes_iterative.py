def is_palindrome_iterative(word):
    start = 0
    end = len(word) - 1
    if not word:
        return False
    for _ in range(start, end):
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True
