def main():
    s1 = input().rstrip()
    s2 = input().rstrip()
    s3 = input().rstrip()
    t = input().rstrip()
    ans = ''
    for i in t:
        if i == '1':
            ans += s1
        elif i == '2':
            ans += s2
        else:
            ans += s3
    print(ans)

if __name__ == '__main__':
    main()