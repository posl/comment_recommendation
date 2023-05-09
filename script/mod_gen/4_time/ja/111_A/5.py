def main():
    n = input()
    print(n.translate(str.maketrans({'1':'9','9':'1'})))

if __name__ == '__main__':
    main()