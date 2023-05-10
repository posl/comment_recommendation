def main():
    # input
    A,B = map(int,input().split())
    # compute
    if (A+B)%2 == 0:
        K = (A+B)//2
    else:
        K = "IMPOSSIBLE"
    # output
    print(K)

if __name__ == '__main__':
    main()