def main():
    N = int(input())
    ans = 0
    while N % 2 == 0:
        N //= 2
        ans += 1
    for i in range(3, int(N**0.5)+1, 2):
        while N % i == 0:
            N //= i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()