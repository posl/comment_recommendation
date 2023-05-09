def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort(reverse=True)
    for i in range(K):
        if i >= N:
            break
        H[i] = 0
    print(sum(H))

if __name__ == '__main__':
    main()