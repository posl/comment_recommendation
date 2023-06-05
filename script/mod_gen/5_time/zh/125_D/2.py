def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if A[i] < 0:
            B.append(-A[i])
        else:
            B.append(A[i])
    if sum(A) >= 0:
        print(sum(B))
    else:
        print(sum(B) - 2 * min(B))

if __name__ == '__main__':
    solve()