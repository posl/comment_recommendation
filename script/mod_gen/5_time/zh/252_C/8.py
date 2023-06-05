def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    ans = 0
    for i in range(10):
        #print(i)
        for j in range(n):
            #print(s[j][i])
            if s[j][i] == '0':
                ans = max(ans, 10)
            elif s[j][i] == '1':
                ans = max(ans, 1)
            elif s[j][i] == '2':
                ans = max(ans, 2)
            elif s[j][i] == '3':
                ans = max(ans, 3)
            elif s[j][i] == '4':
                ans = max(ans, 4)
            elif s[j][i] == '5':
                ans = max(ans, 5)
            elif s[j][i] == '6':
                ans = max(ans, 6)
            elif s[j][i] == '7':
                ans = max(ans, 7)
            elif s[j][i] == '8':
                ans = max(ans, 8)
            elif s[j][i] == '9':
                ans = max(ans, 9)
    print(ans)

if __name__ == '__main__':
    main()