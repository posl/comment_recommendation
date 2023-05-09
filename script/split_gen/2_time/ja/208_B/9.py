def main():
    P = int(input())
    N = 10
    A = [0] * N
    for i in range(N):
        A[N - 1 - i] = P // math.factorial(N - 1 - i)
        P -= A[N - 1 - i] * math.factorial(N - 1 - i)
    print(sum(A))
