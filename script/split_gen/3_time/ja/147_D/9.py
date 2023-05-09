def main():
    N = int(input())
    A = list(map(int, input().split()))
    #全てのXORを求める
    xor_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            xor_sum += A[i] ^ A[j]
    print(xor_sum % (10**9+7))
