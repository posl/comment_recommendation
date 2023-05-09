def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    for i in range(1, N):
        if A[i] != A[i - 1] + 1:
            return -1
    return N - 1
print(solve())

if __name__ == '__main__':
    solve()