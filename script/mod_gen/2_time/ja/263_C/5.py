def main():
    N,M = map(int,input().split())
    for i in range(1,M+1):
        print(i,end=" ")
    print()
    for i in range(2,N+1):
        for j in range(1,M+1):
            if j == 1:
                print(i,end=" ")
            else:
                print(0,end=" ")
        print()
    return

if __name__ == '__main__':
    main()