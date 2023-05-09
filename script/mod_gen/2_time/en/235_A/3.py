def main():
    a, b, c = input()
    print(int(a) + int(b) + int(c) + int(b + c + a) + int(c + a + b))

if __name__ == '__main__':
    main()