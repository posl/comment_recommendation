def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        x = i
        while x != -1:
            x = P[x-1]
            ans += 1
    print(ans)
