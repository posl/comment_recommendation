def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    sum_a = sum(a)
    sum_a2 = sum([i**2 for i in a])
    print(((sum_a**2 - sum_a2) // 2) % mod)

if __name__ == '__main__':
    main()