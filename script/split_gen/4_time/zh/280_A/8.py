def problems280_a():
    h,w = map(int,input().split())
    ans = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                ans += 1
    print(ans)
