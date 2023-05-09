def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    cnt = 0
    for i in range(K,N):
        cnt += H[i]
    print(cnt)

if __name__ == '__main__':
    main()