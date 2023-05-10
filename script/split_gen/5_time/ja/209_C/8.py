def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= 1000000007
    print(ans)
