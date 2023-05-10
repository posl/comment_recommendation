def judge(n, s, t):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                return 'Yes'
    return 'No'
n = int(input())
s = []
t = []
for i in range(n):
    s_i, t_i = input().split()
    s.append(s_i)
    t.append(t_i)
print(judge(n, s, t))

if __name__ == '__main__':
    judge()