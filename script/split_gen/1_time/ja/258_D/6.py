def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A_B = []
    for a, b in zip(A, B):
        A_B.append([a, b])
    A_B.sort()
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A_B[i][0] < A_B[i][1]:
            ans += A_B[i][0]
            X -= 1
        else:
            break
    if X == 0:
        print(ans)
        return
    for i in range(N):
        if X == 0:
            break
        ans += A_B[i][1]
        X -= 1
    print(ans)
