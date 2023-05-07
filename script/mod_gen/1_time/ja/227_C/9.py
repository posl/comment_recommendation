def main():
    N = int(input())
    ans = 0
    for a in range(1,N+1):
        for b in range(a,N//a+1):
            ans += min(N//a//b,N//a-b+1)
    print(ans)

if __name__ == '__main__':
    main()