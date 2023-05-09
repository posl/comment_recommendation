def main():
    # input
    X, Y, A, B = map(int, input().split())
    # compute
    cnt = 0
    while X*A <= X+B and X*A < Y:
        X *= A
        cnt += 1
    cnt += (Y-X-1)//B
    # output
    print(cnt)

if __name__ == '__main__':
    main()