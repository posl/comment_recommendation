def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]
    # compute
    Ss = set(Ss)
    # output
    print(len(Ss))

if __name__ == '__main__':
    main()