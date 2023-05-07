def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] > ans:
            ans = h[i]
    print(ans)
