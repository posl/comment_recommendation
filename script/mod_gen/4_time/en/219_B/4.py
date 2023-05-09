def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    res = ""
    for i in range(len(t)):
        if t[i] == "1":
            res += s1
        elif t[i] == "2":
            res += s2
        else:
            res += s3
    print(res)

if __name__ == '__main__':
    main()