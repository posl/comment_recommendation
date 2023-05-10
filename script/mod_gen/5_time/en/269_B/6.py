def solve():
    s = [input() for _ in range(10)]
    for i in range(10):
        if s[i].count("#") == 1:
            a = i + 1
            break
    for i in range(9, -1, -1):
        if s[i].count("#") == 1:
            b = i + 1
            break
    for i in range(10):
        for j in range(10):
            if s[j][i] == "#":
                c = i + 1
                break
    for i in range(9, -1, -1):
        for j in range(10):
            if s[j][i] == "#":
                d = i + 1
                break
    print(a, b)
    print(c, d)
solve()

if __name__ == '__main__':
    solve()