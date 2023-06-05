def main():
    s = input()
    k = int(input())
    s = s.replace('.',' ')
    s = s.split()
    s = [len(i) for i in s]
    if len(s) == 1:
        print(s[0] + k)
        exit()
    ans = 0
    for i in range(len(s)):
        if i == 0 or i == len(s) - 1:
            ans = max(ans, s[i] + k)
        else:
            ans = max(ans, s[i] + k + 1)
    print(ans)

if __name__ == '__main__':
    main()