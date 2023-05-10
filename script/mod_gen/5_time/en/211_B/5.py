def main():
    # input
    Ss = [input() for _ in range(4)]
    # compute
    # output
    if len(set(Ss)) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()