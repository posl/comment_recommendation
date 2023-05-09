def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans = 0
            continue
        if h[i] <= h[i-1]:
            ans += 1
        else:
            ans = 0
    print(ans)
