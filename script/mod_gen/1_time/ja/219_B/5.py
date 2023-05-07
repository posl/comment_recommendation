def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in range(len(T)):
        if T[i] == '1':
            print(S1, end='')
        elif T[i] == '2':
            print(S2, end='')
        else:
            print(S3, end='')

if __name__ == '__main__':
    main()