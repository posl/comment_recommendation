def main():
    # input
    AB, BC, CA = map(int, input().split())
    # compute
    S = AB * BC // 2
    # output
    print(S)

if __name__ == '__main__':
    main()