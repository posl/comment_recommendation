def main():
    A,B,C,D = map(int,input().split())
    if A <= B*D:
        print(0)
    else:
        if B <= C*D:
            print(-1)
        else:
            print((A-B*D-1)//(B*C-D*B)+1)

if __name__ == '__main__':
    main()