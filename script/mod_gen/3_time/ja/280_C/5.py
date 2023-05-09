def main():
    s = input()
    t = input()
    i = 0
    while i < len(s):
        if s[i] != t[i]:
            print(i+1)
            return
        i += 1
    print(i+1)

if __name__ == '__main__':
    main()