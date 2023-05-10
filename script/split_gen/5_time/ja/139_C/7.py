def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)
