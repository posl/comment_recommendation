def solve():
    n = int(input())
    s = input()
    l = []
    r = []
    for i in range(n):
        if s[i] == 'L':
            l.append(i+1)
        else:
            r.append(i+1)
    r.reverse()
    l.extend(r)
    print(' '.join(map(str,l)))

if __name__ == '__main__':
    solve()