def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    #print(A)
    #print(B)
    ans = 0
    for i in range(N):
        if X > 0:
            if A[i] < B[i]:
                ans += A[i]
                X -= 1
            else:
                ans += B[i]
                X -= 1
        else:
            break
    if X > 0:
        ans += B[0] * X
    print(ans)
