def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    
    ans = []
    for i in range(N):
        if s[i] not in s[:i]:
            ans.append(s[i])
        else:
            ans.append(s[i] + "(" + str(s[:i].count(s[i])) + ")")
    
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()