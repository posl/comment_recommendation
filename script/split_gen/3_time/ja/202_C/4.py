def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    a = [0] * (N + 1)
    b = [0] * (N + 1)
    for i in range(N):
        a[A[i]] += 1
        b[B[C[i]]] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += a[i] * b[i]
    print(ans)
