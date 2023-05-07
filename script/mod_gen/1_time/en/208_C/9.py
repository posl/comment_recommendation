def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    sorted_As = sorted(As)
    #print(sorted_As)
    Ks = [K//N]*N
    #print(Ks)
    K = K%N
    #print(K)
    for i in range(0, K):
        Ks[As.index(sorted_As[i])] += 1
    #print(Ks)
    for i in range(0, N):
        print(Ks[i])

if __name__ == '__main__':
    main()