def main():
    A,B,N = map(int,input().split())
    if N >= B-1:
        print(A*(B-1)//B)
    else:
        print(A*N//B)

if __name__ == '__main__':
    main()