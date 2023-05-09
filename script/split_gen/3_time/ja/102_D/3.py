def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_cum = [0] * (N + 1)
    for i in range(N):
        A_cum[i + 1] = A_cum[i] + A[i]
    ans = 10 ** 9
    for i in range(3, N - 1):
        #print(i)
        #print(A_cum)
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print(A_cum[N] - A_cum[i + 1])
        #print(A_cum[N] - A_cum[i])
        #print(A_cum[i + 1] - A_cum[i])
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]) - (A_cum[i - 1] - A_cum[i - 2]))
        #print()
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print(A_cum[N] - A_cum[i + 1])
        #print(A_cum[N] - A_cum[i])
        #print(A_cum[i + 1] - A_cum[i])
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]) - (A_cum[i - 1] - A_cum[i - 2]))
        #print()
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print
