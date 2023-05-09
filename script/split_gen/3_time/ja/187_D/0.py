def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N - 1, -1, -1):
        a = A[i]
        b = B[i]
        if (a + ans) % b != 0:
            ans += b - ((a + ans) % b)
    print(ans)
