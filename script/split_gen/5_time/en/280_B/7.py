def main():
    N = int(input())
    S = list(map(int, input().split()))
    result = [0] * N
    result[0] = S[0]
    for i in range(1, N):
        result[i] = S[i] - S[i-1]
    print(*result)
