def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = 0
    for i in range(100):
        s += sum([a[j] * (10 ** (100 - i - 1)) for j in range(n)])
        if s > x:
            print(i + 1)
            break

if __name__ == '__main__':
    solve()