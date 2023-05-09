def main():
    import math
    N = int(input())
    ans = 0
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        while N % i == 0:
            N //= i
            ans += 1
    if N > 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()