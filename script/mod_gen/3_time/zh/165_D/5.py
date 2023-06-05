def main():
    A,B,N = map(int,input().split())
    if B > N:
        print((A*N)//B)
    else:
        print((A*(B-1))//B)

if __name__ == '__main__':
    main()