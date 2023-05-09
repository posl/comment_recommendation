def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    bca = int(abc[1] + abc[2] + abc[0])
    cab = int(abc[2] + abc[0] + abc[1])
    print(a+b+c + bca + cab)

if __name__ == '__main__':
    main()