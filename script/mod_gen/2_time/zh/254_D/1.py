def main():
    N = int(input())
    sq = int(N**0.5)
    cnt = 0
    for i in range(1,sq+1):
        for j in range(1,sq+1):
            if i*j <= N:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()