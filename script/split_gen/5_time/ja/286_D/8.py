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
        for j in range(B[i]):
            if X == 0:
                ans = "Yes"
                break
            X -= A[i]
        if ans == "Yes":
            break
    if X <= 0:
        ans = "Yes"
    print(ans)
