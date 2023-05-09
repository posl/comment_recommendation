def main():
    L = int(input())
    N = 20
    M = 60
    print(N,M)
    for i in range(1,N):
        print(i,i+1,0)
    for i in range(1,N):
        print(i,i+1,10**6)
    for i in range(1,N-1):
        print(i,i+2,1)
    L -= 2*(N-1)
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-1)
        L -= 1
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-2)
        L -= 1
    for i in range(1,N-1):
        if L <= 0:
            break
        print(i,i+2,10**6-3)
        L -= 1
main()

if __name__ == '__main__':
    main()