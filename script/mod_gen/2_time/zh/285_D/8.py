def check(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return False
    if s == t[::-1]:
        return False
    return True
n = int(input())
s = []
t = []
for i in range(n):
    s1,t1 = input().split()
    s.append(s1)
    t.append(t1)
flag = True
for i in range(n):
    if check(s[i],t[i]) == False:
        flag = False
        break

if __name__ == '__main__':
    check()