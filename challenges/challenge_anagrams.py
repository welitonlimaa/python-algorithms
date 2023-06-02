from merge_sort import merge_sort


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
