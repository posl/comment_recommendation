def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)
