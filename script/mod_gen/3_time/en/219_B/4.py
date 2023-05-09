def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    d = {'1':s1, '2':s2, '3':s3}
    print(''.join([d[c] for c in t]))

if __name__ == '__main__':
    main()