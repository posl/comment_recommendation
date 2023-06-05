def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.append(K+1)
    for i in range(N):
        print((K-a[i]+1)//N)

if __name__ == '__main__':
    main()