def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 10**6
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()