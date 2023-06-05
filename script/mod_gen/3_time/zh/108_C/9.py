def main():
    N,K = map(int,input().split())
    cnt = 0
    for i in range(1,N+1):
        if i%K == 0:
            cnt += 1
        elif K%2 == 0:
            if i%K == K/2:
                cnt += 1
    print(cnt**3)

if __name__ == '__main__':
    main()