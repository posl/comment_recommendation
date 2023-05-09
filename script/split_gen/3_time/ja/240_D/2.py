def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (max(A) + 1)
    for a in A:
        B[a] += 1
    cnt = 0
    for i in range(2, max(A) + 1):
        cnt += B[i] // i
        B[i] = B[i] % i
        B[i + 1] += B[i]
    print(N - cnt)
