def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if (b - a) > k:
        print(':(')
    elif (c - b) > k:
        print(':(')
    elif (d - c) > k:
        print(':(')
    elif (e - d) > k:
        print(':(')
    else:
        print('Yay!')

if __name__ == '__main__':
    main()