def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return "".join(result)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return "", "", False

    sorted_string1 = merge_sort(first_string.lower())
    sorted_string2 = merge_sort(second_string.lower())

    return sorted_string1, sorted_string2, sorted_string1 == sorted_string2
