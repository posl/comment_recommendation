def solve():
    n = int(input())
    names = set()
    for _ in range(n):
        s, t = input().split()
        if (s, t) in names:
            print('Yes')
            return
        else:
            names.add((s, t))
    print('No')

if __name__ == '__main__':
    solve()