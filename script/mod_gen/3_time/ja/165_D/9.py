def main():
    A,B,N = map(int,input().split())
    print(A*min(B-1,N)//B)

if __name__ == '__main__':
    main()