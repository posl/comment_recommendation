def main():
    abc = input()
    a, b, c = abc[0], abc[1], abc[2]
    print(int(a + b + c) + int(b + c + a) + int(c + a + b))
main()

if __name__ == '__main__':
    main()