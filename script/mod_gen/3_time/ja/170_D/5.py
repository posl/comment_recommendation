def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_a_divisors = [0] * (max_a + 1)
    for i in range(n):
        max_a_divisors[a[i]] += 1
    ans = 0
    for i in range(1, max_a + 1):
        if max_a_divisors[i] == 1:
            for j in range(i * 2, max_a + 1, i):
                max_a_divisors[j] = 0
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()