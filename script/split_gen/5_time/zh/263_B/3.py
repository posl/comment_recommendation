def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        x = i + 1
        while x != -1:
            x = P[x - 1]
            ans += 1
            if x == 0:
                break
    print(ans)
