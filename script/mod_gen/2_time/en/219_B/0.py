def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in t:
        if i == '1':
            print(s1, end='')
        elif i == '2':
            print(s2, end='')
        elif i == '3':
            print(s3, end='')
main()

if __name__ == '__main__':
    main()