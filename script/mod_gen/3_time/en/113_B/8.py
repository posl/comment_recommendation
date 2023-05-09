def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 100000000000000
    for i in range(n):
        if min > abs(t - h[i] * 0.006 - a):
            min = abs(t - h[i] * 0.006 - a)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()