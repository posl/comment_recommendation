def main():
    S = input()
    s = S[0]
    for i in S[1:-1]:
        if i.isalpha():
            if s.isalpha():
                s += i
            else:
                s = i
        else:
            if s.isalpha():
                s = i
            else:
                s += i
    s += S[-1]
    if s == S:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()