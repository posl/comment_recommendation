def main():
    n = int(input())
    w = list(map(int, input().split()))
    w_sum = sum(w)
    min_diff = w_sum
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = w_sum - s1
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()