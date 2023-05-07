def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == ans + 1:
            ans += 1
    if ans == 0:
        print(-1)
    else:
        print(N - ans)
