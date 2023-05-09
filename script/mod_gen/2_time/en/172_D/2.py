def main():
    N = int(input())
    divisors = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            divisors[j] += 1
    ans = 0
    for i in range(1, N+1):
        ans += i * divisors[i]
    print(ans)

if __name__ == '__main__':
    main()