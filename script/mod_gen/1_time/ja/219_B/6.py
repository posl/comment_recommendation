def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for t in T:
        if t == '1':
            print(S1, end='')
        elif t == '2':
            print(S2, end='')
        elif t == '3':
            print(S3, end='')

if __name__ == '__main__':
    main()