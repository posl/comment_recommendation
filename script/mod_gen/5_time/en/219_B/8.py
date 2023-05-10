def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    out = ""
    for i in range(len(t)):
        if t[i] == "1":
            out += s1
        elif t[i] == "2":
            out += s2
        else:
            out += s3
    print(out)

if __name__ == '__main__':
    main()