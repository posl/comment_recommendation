def solve():
    N = int(input())
    A = list(map(int, input().split()))
    res = 0
    while all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        res += 1
    print(res)

if __name__ == '__main__':
    solve()