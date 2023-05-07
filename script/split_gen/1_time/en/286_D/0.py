def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = "No"
    for i in range(N):
        if X == A[i] * B[i]:
            ans = "Yes"
            break
        elif X > A[i] * B[i]:
            X -= A[i] * B[i]
        else:
            ans = "No"
            break
    print(ans)
