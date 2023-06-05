def check(s,t):
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                return True
    return False
n = int(input())
s = []
t = []
for i in range(n):
    s.append(input().split()[0])
    t.append(input().split()[1])
for i in range(n):
    for j in range(n):
        if i != j:
            if s[i] == s[j] or t[i] == t[j]:
                print('Yes')
                exit()
print('No')

if __name__ == '__main__':
    check()