def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = []
    for i in t:
        if i == '1':
            s.append(s1)
        elif i == '2':
            s.append(s2)
        else:
            s.append(s3)
    print(''.join(s))

if __name__ == '__main__':
    main()