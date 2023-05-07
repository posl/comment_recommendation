def main():
    #input
    N = int(input())
    Ss = [input() for _ in range(N)]
    #compute
    Ss.sort()
    ans = 1
    for i in range(1,N):
        if Ss[i] != Ss[i-1]:
            ans += 1
    #output
    print(ans)

if __name__ == '__main__':
    main()