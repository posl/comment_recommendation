def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            continue
        B.append(A[i])
    A = B
    N = len(A)
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] != 0:
                continue
            for k in range(N):
                if A[i] // A[j] == A[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()