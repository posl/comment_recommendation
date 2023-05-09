def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = ""
    for i in range(len(t)):
        if t[i] == "1":
            s += s1
        elif t[i] == "2":
            s += s2
        elif t[i] == "3":
            s += s3
    print(s)

if __name__ == '__main__':
    main()