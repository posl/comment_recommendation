def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    if i == len(s)-1:
        print(len(s)+1)

if __name__ == '__main__':
    main()