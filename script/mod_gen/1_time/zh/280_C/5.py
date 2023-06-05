def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
        elif i == len(s) - 1:
            print(i+2)
            break

if __name__ == '__main__':
    main()