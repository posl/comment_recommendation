def solve():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda s: ''.join(map(lambda c: chr(x.index(c) + 97), s)))
    print('\n'.join(s))
solve()

if __name__ == '__main__':
    solve()