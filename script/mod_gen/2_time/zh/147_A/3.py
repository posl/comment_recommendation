def main():
    # input
    A_1, A_2, A_3 = map(int, input().split())
    # check
    if A_1 + A_2 + A_3 >= 22:
        # output
        print('bust')
    else:
        # output
        print('win')

if __name__ == '__main__':
    main()