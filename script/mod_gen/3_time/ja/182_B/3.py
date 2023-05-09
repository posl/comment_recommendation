def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcd = [0] * 1001
    for i in a:
        for j in range(1, i + 1):
            if i % j == 0:
                gcd[j] += 1
    print(gcd.index(max(gcd)))

if __name__ == '__main__':
    main()