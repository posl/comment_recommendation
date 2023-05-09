def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) / 2
    print(int(ans))
