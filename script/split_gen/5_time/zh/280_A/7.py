def count_chess():
    h,w = input().split()
    h = int(h)
    w = int(w)
    count = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                count += 1
    return count
