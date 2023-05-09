def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B, C = [], []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    ans = [0] * Q
    ans[0] = sum(A)
    for i in range(1, Q):
        ans[i] = ans[i-1] + (C[i] - B[i]) * A.count(B[i])
    for i in range(Q):
        print(ans[i])
