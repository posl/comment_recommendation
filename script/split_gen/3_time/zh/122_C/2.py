def solve():
    n, q = map(int, input().split())
    s = input()
    #print(n, q, s)
    ac = [0] * (n + 1)
    for i in range(1, n):
        if s[i - 1] == 'A' and s[i] == 'C':
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]
    for i in range(q):
        l, r = map(int, input().split())
        print(ac[r] - ac[l])
