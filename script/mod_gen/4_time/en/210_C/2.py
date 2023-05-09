def main():
    N,K = map(int,input().split())
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N-K+1):
        tmp = len(set(C[i:i+K]))
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()