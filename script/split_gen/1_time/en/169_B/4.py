def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans = ans * A[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)
