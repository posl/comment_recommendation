def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    ans = -1
    for i in range(k + 1):
        if (sum_a + i) / n >= m:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()