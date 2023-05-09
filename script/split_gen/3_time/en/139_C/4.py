def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            ans += 1
        else:
            ans = 0
    print(ans)
    return 0
