def main():
    x = input()
    n = int(input())
    s = []
    for i in range(0,n):
        s.append(input())
    x_dict = {}
    for i in range(0,26):
        x_dict[x[i]] = chr(ord('a')+i)
    for i in range(0,n):
        for j in range(0,len(s[i])):
            s[i] = s[i].replace(s[i][j],x_dict[s[i][j]])
    s.sort()
    for i in range(0,n):
        for j in range(0,len(s[i])):
            s[i] = s[i].replace(s[i][j],x[j])
    for i in range(0,n):
        print(s[i])
main()
