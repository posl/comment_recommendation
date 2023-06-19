def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    for i in range(K):
        if B[i] in A:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()