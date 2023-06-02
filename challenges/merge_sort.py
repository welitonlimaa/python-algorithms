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