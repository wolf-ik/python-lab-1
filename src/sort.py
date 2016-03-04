def radix_sort(lst, radix=10):
    max_len = 32
    for x in range(max_len):
        bins = [[] for i in range(radix)]
        for y in lst:
            bins[(y/10**x) % radix].append(y)
        lst = []
        for section in bins:
            lst.extend(section)
    return lst


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        return quick_sort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + quick_sort([x for x in lst[1:] if x >= lst[0]])


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def sort_handler(array, method='quick'):
    sort_mapping = {
        'radix': radix_sort,
        'quick': quick_sort,
        'merge': merge_sort,
    }
    sort_func = sort_mapping.get(method)
    if sort_func is None:
        return 'Please, enter valid method.'
    return sort_func(array)
