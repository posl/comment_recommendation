def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    sum = 0
    minus = 0
    min_abs = float('inf')
    for i in range(n):
        sum += abs(a[i])
        if a[i] < 0:
            minus += 1
        min_abs = min(min_abs, abs(a[i]))
    if minus % 2 == 0:
        ans = sum
    else:
        ans = sum - 2 * min_abs
    print(ans)

if __name__ == '__main__':
    main()