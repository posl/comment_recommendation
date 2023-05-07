def main():
    # input
    R, C = map(int, input().split())
    # compute
    if (R*C)%2 == 0:
        ans = 'black'
    else:
        ans = 'white'
    # output
    print(ans)

if __name__ == '__main__':
    main()