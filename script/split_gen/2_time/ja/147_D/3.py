def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += A[i] ^ A[j]
    print(sum % (10**9 + 7))
