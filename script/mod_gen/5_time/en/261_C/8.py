def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if i == 0:
            print(s[i])
        else:
            if s[i] in s[:i]:
                cnt = 0
                for j in range(i):
                    if s[j] == s[i]:
                        cnt += 1
                print(s[i] + "(" + str(cnt) + ")")
            else:
                print(s[i])

if __name__ == '__main__':
    main()