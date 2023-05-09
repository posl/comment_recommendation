def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    output = ''
    for i in T:
        if i == '1':
            output += S1
        elif i == '2':
            output += S2
        else:
            output += S3
    print(output)

if __name__ == '__main__':
    main()