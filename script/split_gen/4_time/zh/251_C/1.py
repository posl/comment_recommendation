def solve(n, s, t):
    dic = {}
    for i in range(n):
        if s[i] not in dic:
            dic[s[i]] = [t[i], i]
        else:
            if t[i] > dic[s[i]][0]:
                dic[s[i]] = [t[i], i]
    max = 0
    for key in dic:
        if dic[key][0] > max:
            max = dic[key][0]
            index = dic[key][1]
    return index
n = int(input())
s = []
t = []
for i in range(n):
    temp = input().split()
    s.append(temp[0])
    t.append(int(temp[1]))
print(solve(n, s, t))
