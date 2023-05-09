def main():
    # input
    S = input()
    # compute
    S_list = list(S)
    S_list.sort()
    # output
    print(''.join(S_list))

if __name__ == '__main__':
    main()