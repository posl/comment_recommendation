def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        else:
            if h[i] >= h[i-1]:
                ans += h[i] - h[i-1]
    print(ans)
main()
