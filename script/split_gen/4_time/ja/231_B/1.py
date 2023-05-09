def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    #print(dic)
    max = 0
    ans = ""
    for k,v in dic.items():
        if v > max:
            max = v
            ans = k
    print(ans)
