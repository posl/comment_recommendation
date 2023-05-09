def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = 100000000
    for i in range(n):
        if diff > abs(a - (t - h[i] * 0.006)):
            diff = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()