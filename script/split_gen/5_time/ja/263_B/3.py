def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += 1
        p = P[i] - 1
        while p != 0:
            ans += 1
            p = P[p] - 1
    print(ans)
