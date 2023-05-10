def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(N-K):
        if a[i] > a[i+K]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()