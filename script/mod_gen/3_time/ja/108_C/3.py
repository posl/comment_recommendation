def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        if i%K == 0:
            ans += 1
    print(ans**3)

if __name__ == '__main__':
    main()