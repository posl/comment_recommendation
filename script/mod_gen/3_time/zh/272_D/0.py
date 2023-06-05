def main():
    N,M = map(int,input().split())
    print(N,M)
    for i in range(N):
        for j in range(N):
            print(i,j)
            print((i-j)**2)
            print((i-j)**2+(i-j)**2)
            print((i-j)**2+(i-j)**2)**(1/2)
            print(M**(1/2))
            print(((i-j)**2+(i-j)**2)**(1/2)<=M**(1/2))
            if (((i-j)**2+(i-j)**2)**(1/2)<=M**(1/2)):
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    main()