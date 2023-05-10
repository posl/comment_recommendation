def solve():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) == abs(i - j):
                return 'No'
    return 'Yes'
print(solve())

if __name__ == '__main__':
    solve()