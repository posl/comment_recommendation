def main():
    s = list(input())
    t = list(input())
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i+1)
            break
    else:
        print(len(s)+1)

if __name__ == '__main__':
    main()