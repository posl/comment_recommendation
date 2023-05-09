def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                cnt += 1
                N //= i
            for j in range(1, 100):
                if cnt >= j:
                    cnt -= j
                    ans += 1
                else:
                    break
    if N != 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()