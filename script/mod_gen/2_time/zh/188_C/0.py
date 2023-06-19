def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        return merge(left, right)

if __name__ == '__main__':
    merge_sort()