def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if abs(t - h[i] * 0.006 - a) < abs(t - h[ans - 1] * 0.006 - a):
            ans = i + 1
    print(ans)
main()
