def solve():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[-1] < sum(l[:-1]):
        print

if __name__ == '__main__':
    solve()