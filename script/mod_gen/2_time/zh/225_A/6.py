def main():
    S = input()
    a = S[0]
    b = S[1]
    c = S[2]
    if a == b == c:
        print(1)
    elif a == b or b == c or c == a:
        print(3)
    else:
        print(6)

if __name__ == '__main__':
    main()