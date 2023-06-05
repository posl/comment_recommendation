def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    max = 0
    for i in range(n):
        if s.count(s[i]) > max:
            max = s.count(s[i])
            name = s[i]
    print(name)

if __name__ == '__main__':
    solve()