def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    s.sort()
    #print(s)
    for i in range(n-1):
        if s[i] == s[i+1]:
            print("存在不满足的字符串")
            print(s[i])
            return
    print("可满足")
    return
