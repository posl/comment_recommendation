def solve():
    s = []
    for i in range(10):
        s.append(input())
    for i in range(10):
        if s[i].count('#') != 4:
            continue
        for j in range(10):
            if s[j][i] != '#':
                continue
            print(i+1, j+1)
            return
solve()
