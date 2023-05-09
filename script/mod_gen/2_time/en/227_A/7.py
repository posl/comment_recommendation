def main():
    N,K,A = map(int,input().split())
    if K <= N:
        print(K)
    elif K > N:
        print(N - (K - N))

if __name__ == '__main__':
    main()