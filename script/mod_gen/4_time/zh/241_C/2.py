def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    #print(s[0][0])
    #print(s[0][1])
    #print(s[1][0])
    #print(s[1][1])
    #print(s[0][0] == s[0][1])
    #print(s[1][0] == s[1][1])
    #print(s[0][0] == s[1][0])
    #print(s[0][1] == s[1][1])
    #print(s[0][0] == s[1][1])
    #print(s[0][1] == s[1][0])
    #print(s[0][0] == s[1][0])
    #print(s[0][1] == s[1][1])
    #print(s[0][0] == s[1][1])
    #print(s[0][1] == s[1][0])
    #print(s[0][0] == s[1][0])
    #print(s[0][1] == s[1][1])
    #print(s[0][0] == s[1][1])
    #print(s[0][1] == s[1][0])
    #print(s[0][0] == s[1][0])
    #print(s[0][1] == s[1][1])
    #print(s[0][0] == s[1][1])
    #print(s[0][1] == s[1][0])
    #print(s[0][0] == s[1][0])
    #print(s[0][1] == s[1][1])
    #print(s[0][0] == s[1][1])
    #print(s[0][1] == s[1][0])
    for i in range(n):
        for j in range(n):
            if i < n - 1 and j < n - 1:
                if s[i][j] == s[i][j + 1] and s[i][j] == s[i + 1][j] and s[i][j] == s[i + 1][j + 1]:
                    return print('

if __name__ == '__main__':
    solve()