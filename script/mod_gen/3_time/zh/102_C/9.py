def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(n)]
    A.sort()
    b = A[n // 2]
    print(sum(abs(a - b) for a in A))

if __name__ == '__main__':
    solve()