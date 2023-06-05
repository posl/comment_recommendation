def problems285_d():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s1, t1 = input().split()
        s.append(s1)
        t.append(t1)
    #print(s)
    #print(t)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == t[j]:
                    s[i], t[i] = t[i], s[i]
    #print(s)
    #print(t)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    problems285_d()