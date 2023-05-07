def main():
    abc = input()
    print(int(abc) + int(abc[::-1]) + int(abc[1:] + abc[0]))

if __name__ == '__main__':
    main()