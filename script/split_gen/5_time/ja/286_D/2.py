def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 'No'
    for i in range(N):
        if A[i] <= X and B[i] > 0:
            ans = 'Yes'
            break
    print(ans)
