def main():
    # input
    S = input()
    # compute
    # output
    print(S[::-1].translate(str.maketrans('01689', '01986')))

if __name__ == '__main__':
    main()