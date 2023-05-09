def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = []
    for i in t:
        if i == '1':
            ans.append(s1)
        elif i == '2':
            ans.append(s2)
        elif i == '3':
            ans.append(s3)
    print("".join(ans))

if __name__ == '__main__':
    main()