def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a + b + c + b*10 + c*100 + c*10 + a*100 + a*10 + b*100)

if __name__ == '__main__':
    main()