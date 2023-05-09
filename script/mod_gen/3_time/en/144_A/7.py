def main():
    #input
    A,B = map(int,input().split())
    #calculation
    if A > 9 or B > 9:
        print(-1)
    else:
        print(A*B)
    #output

if __name__ == '__main__':
    main()