def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    if K==1:
        print("Yes")
        return
    if N==K:
        print("No")
        return
    for i in range(N-K):
        if A[i]>A[i+K]:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()