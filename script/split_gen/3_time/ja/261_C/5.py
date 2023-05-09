def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]] += 1
            print(s[i] + '(' + str(dic[s[i]]-1) + ')')
        else:
            dic[s[i]] = 1
            print(s[i])
