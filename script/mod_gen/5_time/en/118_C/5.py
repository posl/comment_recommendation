def solve(N, A):
    while len(A) > 1:
        A.sort()
        A[-1] = A[-1] % A[0]
        if A[-1] == 0:
            A.pop(-1)
    return A[0]
N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

if __name__ == '__main__':
    solve()