def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
    else:
        for i in range(len(s)):
            if s[i] != '1':
                print(s[i])
                break

if __name__ == '__main__':
    main()