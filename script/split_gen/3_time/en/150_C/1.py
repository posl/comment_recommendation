def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    p = 0
    q = 0
    for i in range(N):
        p += P[i] * pow(10, N - i - 1)
        q += Q[i] * pow(10, N - i - 1)
    print(abs(p - q))
