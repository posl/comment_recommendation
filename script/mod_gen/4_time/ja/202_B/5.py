def main():
    S = input()
    S = S[::-1]
    S = S.replace("6", "a")
    S = S.replace("9", "6")
    S = S.replace("a", "9")
    S = S.replace("0", "a")
    S = S.replace("1", "0")
    S = S.replace("a", "1")
    print(S)

if __name__ == '__main__':
    main()