def main():
    C = input()
    if C == 'z':
        print('z')
    else:
        print(chr(ord(C)+1))

if __name__ == '__main__':
    main()