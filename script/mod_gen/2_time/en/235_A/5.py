def main():
    abc = input()
    abc1 = abc[0]
    abc2 = abc[1]
    abc3 = abc[2]
    bca = abc2 + abc3 + abc1
    cab = abc3 + abc1 + abc2
    print(int(abc)+int(bca)+int(cab))

if __name__ == '__main__':
    main()