def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,X,A)
    count = 1
    friend = X
    while True:
        friend = A[friend-1]
        if friend == X:
            break
        count += 1
    print(count)

if __name__ == '__main__':
    main()