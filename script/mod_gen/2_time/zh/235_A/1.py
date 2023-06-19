def main():
    abc = raw_input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print a*111 + b*11 + c*1 + b*100 + c*10 + a*1 + c*100 + a*10 + b*1

if __name__ == '__main__':
    main()