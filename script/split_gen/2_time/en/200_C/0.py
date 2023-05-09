def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                ans += 1
    print(ans)
