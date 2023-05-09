def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[n-1])

if __name__ == '__main__':
    solve()