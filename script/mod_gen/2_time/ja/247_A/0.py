def main():
    s = input()
    for i in range(3):
        if s[i] == "1":
            s = s[:i] + "0" + s[i+1:]
        else:
            s = s[:i] + "0" + s[i+1:]
    if s[3] == "1":
        s = s[:3] + "0"
    print(s)

if __name__ == '__main__':
    main()