def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 1
    min_diff = abs(a - (t - h[0] * 0.006))
    for i in range(1, n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)
main()

if __name__ == '__main__':
    main()