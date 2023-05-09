def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    # output
    print(5-len(set([A, B, C, D, E]))+1)

if __name__ == '__main__':
    main()