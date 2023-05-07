def main():
    N = int(input())
    cnt = 0
    for p in range(2, int(N ** 0.5) + 1):
        q = 1
        while True:
            q *= p
            if q > N:
                break
            if q % 250 == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()