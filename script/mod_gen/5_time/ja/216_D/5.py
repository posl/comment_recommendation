def main():
    N,M = map(int,input().split())
    K = []
    A = []
    for i in range(M):
        K.append(int(input()))
        A.append(list(map(int,input().split())))
    print(N,M,K,A)

if __name__ == '__main__':
    main()