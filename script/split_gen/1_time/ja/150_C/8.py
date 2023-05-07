def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    def count_permutation(N, P):
        count = 0
        for i in range(1, N):
            count += i * math.factorial(N - i)
            for j in range(i + 1, N):
                if P[i - 1] < P[j - 1]:
                    count -= math.factorial(N - i - 1)
        return count
    print(abs(count_permutation(N, P) - count_permutation(N, Q)))
