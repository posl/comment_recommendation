def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    a, b = 0, 0
    for i in range(N):
        a += P[i] * (N - i) * ((N - i) - 1) // 2
        b += Q[i] * (N - i) * ((N - i) - 1) // 2
    print(abs(a - b))
