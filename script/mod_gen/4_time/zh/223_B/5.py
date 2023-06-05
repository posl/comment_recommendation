def main():
    s = input()
    a = [s]
    for i in range(len(s)):
        s = s[1:]+s[0]
        a.append(s)
    print(min(a))
    print(max(a))

if __name__ == '__main__':
    main()