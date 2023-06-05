def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in range(len(t)):
        if t[i] == '1':
            print(s1,end='')
        elif t[i] == '2':
            print(s2,end='')
        else:
            print(s3,end='')
    print()

if __name__ == '__main__':
    main()