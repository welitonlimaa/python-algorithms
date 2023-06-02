def merge_sort(word_list, start=0, end=None):
    if end is None:
        end = len(word_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word_list, start, mid)
        merge_sort(word_list, mid, end)
        merge(word_list, start, mid, end)


def merge(word_list, start, mid, end):
    left = word_list[start:mid]
    right = word_list[mid:end]

    left_index, right_index = 0, 0
    for general_index in range(start, end):
        if left_index >= len(left):
            word_list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word_list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word_list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word_list[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_char_list = list(first_string.lower())
    merge_sort(first_char_list, 0, len(first_string))
    first_string_sorted = ''.join(first_char_list)
    second_char_list = list(second_string.lower())
    merge_sort(second_char_list, 0, len(second_string))
    second_string_sorted = ''.join(second_char_list)

    if not first_string_sorted or not second_string_sorted:
        return (
            first_string_sorted,
            second_string_sorted,
            False
        )   
    return (
        first_string_sorted,
        second_string_sorted,
        first_string_sorted == second_string_sorted
    )


print(is_anagram("amor", "roma"))
