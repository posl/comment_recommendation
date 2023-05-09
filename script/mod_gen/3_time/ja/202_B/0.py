def main():
    s = list(input())
    s.reverse()
    for i in range(len(s)):
        if s[i] == "6":
            s[i] = "9"
        elif s[i] == "9":
            s[i] = "6"
    print("".join(s))

if __name__ == '__main__':
    main()