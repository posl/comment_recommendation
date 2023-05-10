def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if abs(A[i]-B[i])>K:
            return "No"
    return "Yes"
print(solve())

if __name__ == '__main__':
    solve()