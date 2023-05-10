def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for i in range(K.bit_length(), -1, -1):
        count = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                count += 1
        if count < N - count and result + (1 << i) <= K:
            result += 1 << i
    for i in range(N):
        result += A[i] ^ result
    print(result)
