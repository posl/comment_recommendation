def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ''
    for i in T:
        if i == '1':
            ans += S1
        elif i == '2':
            ans += S2
        else:
            ans += S3
    print(ans)

if __name__ == '__main__':
    main()