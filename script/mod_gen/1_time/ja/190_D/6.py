def main():
    N = int(input())
    cnt = 0
    for i in range(1, 10**6 + 1):
        if (2*N) % i == 0:
            if (2*N)//i % 2 == 1:
                cnt += 1
            if (2*N)//i % 2 == 0 and (2*N)//i//2 - i//2 > 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()