def merge(chars, start, middle, end):
    left = chars[start:middle]
    right = chars[middle:end]

    left_index, right_index = 0, 0

    for i in range(start, end):
        if left_index >= len(left):
            chars[i] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            chars[i] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            chars[i] = left[left_index]
            left_index += 1
        else:
            chars[i] = right[right_index]
            right_index += 1


def sort_string(chars, start=0, end=None):
    if not end:
        end = len(chars)
    if (end - start) > 1:
        middle = (start + end) // 2
        sort_string(chars, start, middle)
        sort_string(chars, middle, end)
        merge(chars, start, middle, end)


def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())
    sort_string(first_string_list)
    sort_string(second_string_list)
    first_string_sorted = ''.join(first_string_list)
    second_string_sorted = ''.join(second_string_list)
    if not first_string_sorted or not second_string_sorted:
        return (first_string_sorted, second_string_sorted, False)
    return (
            first_string_sorted,
            second_string_sorted,
            first_string_sorted == second_string_sorted
    )
