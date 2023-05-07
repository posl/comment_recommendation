def solve():
    n = int(input())
    s = input()
    k = s.count('"')
    for i in range(n):
        if s[i] == ',' and k % 2 == 0:
            print('.', end='')
        else:
            print(s[i], end='')
        if s[i] == '"':
            k -= 1

if __name__ == '__main__':
    solve()