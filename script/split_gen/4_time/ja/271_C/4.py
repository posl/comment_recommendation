def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(N):
        ans *= A[i] - i
        ans %= 10**9 + 7
        if ans == 0:
            break
    print(ans)
