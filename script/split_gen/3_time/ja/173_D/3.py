def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * (2 ** i)
    print(ans)
