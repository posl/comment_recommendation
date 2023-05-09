def main():
    # input
    A_1, A_2, A_3, A_4 = map(int, input().split())
    # compute
    # output
    if A_1 + A_2 + A_3 + A_4 >= 22:
        print("bust")
    else:
        print("win")

if __name__ == '__main__':
    main()