def main():
    S = input()
    S = S[::-1]
    S = S + '000'
    S = S[::-1]
    S = int(S)
    count = 0
    while S != 0:
        if S >= 100:
            count += S // 100
            S = S % 100
        elif S >= 10:
            count += S // 10
            S = S % 10
        else:
            count += S
            S = 0
    print(count)

if __name__ == '__main__':
    main()