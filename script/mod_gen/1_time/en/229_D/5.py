def main():
    # input
    S = input()
    K = int(input())
    # compute
    # output
    print(max([len(s) for s in S.replace('.', ' ').split()]))

if __name__ == '__main__':
    main()