def main():
    # input
    S = input()
    # compute
    # output
    print(S[::-1].translate(str.maketrans({'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'})))

if __name__ == '__main__':
    main()