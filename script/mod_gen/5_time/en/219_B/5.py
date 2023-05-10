def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = ""
    for i in t:
        if i == "1":
            s += s1
        elif i == "2":
            s += s2
        else:
            s += s3
    print(s)

if __name__ == '__main__':
    main()