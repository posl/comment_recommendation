def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    
    s = ''
    for i in T:
        if i == '1':
            s += S1
        elif i == '2':
            s += S2
        else:
            s += S3
    print(s)

if __name__ == '__main__':
    main()