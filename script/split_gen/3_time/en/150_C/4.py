def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    Q = [int(x) for x in input().split()]
    a = 0
    b = 0
    for i in range(N):
        a += P[i] * (N - i) * math.factorial(N - i - 1)
        b += Q[i] * (N - i) * math.factorial(N - i - 1)
    print(abs(a - b))
