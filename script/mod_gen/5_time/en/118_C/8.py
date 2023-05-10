def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    import math
    print(math.gcd(a[0], a[-1]))

if __name__ == '__main__':
    solve()