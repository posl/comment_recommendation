def main():
    abc = list(input())
    bca = [abc[1], abc[2], abc[0]]
    cab = [abc[2], abc[0], abc[1]]
    print(int("".join(abc)) + int("".join(bca)) + int("".join(cab)))

if __name__ == '__main__':
    main()