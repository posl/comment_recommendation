def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (N - 1 - i) * i
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            ans -= N - 1 - i
    print(ans)
