def solve():
    s = input()
    k = int(input())
    size = len(s)
    if k <= size:
        print(s[k-1])
        return
    i = 0
    while i < size:
        if s[i] == '1':
            i += 1
            continue
        j = i
        while j < size and s[j] == s[i]:
            j += 1
        if j - i >= k:
            print(s[i])
            return
        k -= j - i
        i = j
    print(1)
