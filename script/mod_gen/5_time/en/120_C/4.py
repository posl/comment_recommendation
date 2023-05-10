def main():
    # input
    S = input()
    N = len(S)
    # compute
    # output
    print(min(S.count('0'), S.count('1'))*2)

if __name__ == '__main__':
    main()