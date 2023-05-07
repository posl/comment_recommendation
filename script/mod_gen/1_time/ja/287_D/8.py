def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        s1 = s[:i]
        s2 = s[-(len(t)-i):]
        if s1.count("?") + s2.count("?") + len(t) - i - s1.count("?") - s2.count("?") == len(t):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()