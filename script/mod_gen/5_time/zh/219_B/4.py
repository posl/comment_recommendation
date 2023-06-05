def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    out = ""
    for i in t:
        if i == "1":
            out += s1
        elif i == "2":
            out += s2
        elif i == "3":
            out += s3
    print(out)

if __name__ == '__main__':
    main()