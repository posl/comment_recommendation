def main():
    N,A,B,C,D,E = map(int, input().split())
    print((N-1)//min(A,B,C,D,E)+5)

if __name__ == '__main__':
    main()