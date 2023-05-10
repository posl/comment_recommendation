def solve():
    s = input()
    ans = 0
    for i in range(10000):
        t = str(i).zfill(4)
        ok = True
        for j in range(10):
            if s[j] == 'o' and t.find(str(j)) == -1:
                ok = False
            if s[j] == 'x' and t.find(str(j)) != -1:
                ok = False
        if ok:
            ans += 1
    print(ans)
solve()
