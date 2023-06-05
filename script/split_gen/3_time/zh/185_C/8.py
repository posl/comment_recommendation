def count_cut(l):
    if l < 12:
        return 0
    elif l == 12:
        return 1
    else:
        return count_cut(l-1) + count_cut(l-2) + count_cut(l-3) + count_cut(l-4) + count_cut(l-5) + count_cut(l-6)
l = int(input())
print(count_cut(l))
