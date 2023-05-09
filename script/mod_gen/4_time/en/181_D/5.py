def solve():
    s = input()
    if len(s) == 1:
        return 'Yes' if int(s) % 8 == 0 else 'No'
    if len(s) == 2:
        return 'Yes' if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0 else 'No'
    d = {}
    for i in range(1, 10):
        d[str(i)] = 0
    for i in s:
        d[i] += 1
    for i in range(112, 1000, 8):
        t = {}
        for j in range(1, 10):
            t[str(j)] = 0
        for j in str(i):
            t[j] += 1
        ok = True
        for j in range(1, 10):
            if t[str(j)] > d[str(j)]:
                ok = False
                break
        if ok:
            return 'Yes'
    return 'No'
print(solve())

if __name__ == '__main__':
    solve()