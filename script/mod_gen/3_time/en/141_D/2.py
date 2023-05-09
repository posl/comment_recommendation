def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] //= 2
    A.sort(reverse=True)
    return sum(A)
print(solve())

if __name__ == '__main__':
    solve()