def main():
    s = input()
    s = s.replace('RL', 'R L')
    s = list(s.split())
    ans = []
    for i in range(len(s)):
        if i == 0:
            ans.append(0)
        elif i == len(s)-1:
            ans.append(0)
        else:
            if len(s[i]) % 2 == 0:
                ans.append(len(s[i])//2)
                ans.append(len(s[i])//2)
            else:
                if s[i][0] == 'R':
                    ans.append(len(s[i])//2)
                    ans.append(len(s[i])//2+1)
                else:
                    ans.append(len(s[i])//2+1)
                    ans.append(len(s[i])//2)
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()