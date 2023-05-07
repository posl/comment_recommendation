def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        elif h[i] > h[i-1]:
            ans += h[i] - h[i-1]
    print(ans)
