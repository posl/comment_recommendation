def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    cnt = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                cnt += 1
            if cnt == k:
                print(s[i]+s[j])
                exit()
        cnt += 1
        if cnt == k:
            print(s[i]+s[i])
            exit()

if __name__ == '__main__':
    main()