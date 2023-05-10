def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_diff = 10000000
    min_diff_index = 0
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            min_diff_index = i + 1
    print(min_diff_index)

if __name__ == '__main__':
    main()