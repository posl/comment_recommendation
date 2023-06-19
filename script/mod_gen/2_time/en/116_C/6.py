def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            ans += max(0, h[i] - h[i-1])
    print(ans)
main()
