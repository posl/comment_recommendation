def problems285_b():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        while i + l < n:
            if s[l] != s[i + l]:
                l += 1
            else:
                break
        print(l)
