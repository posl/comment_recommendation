def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if A[j] % A[i] == 0:
                B[i] += 1
    ans = 0
    for i in range(N):
        if B[i] == 0:
            ans += 1
    print(ans)
