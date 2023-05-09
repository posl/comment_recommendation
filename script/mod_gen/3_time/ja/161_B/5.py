def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for a in A:
        sum += a
    if A[M-1] >= sum / (4 * M):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()