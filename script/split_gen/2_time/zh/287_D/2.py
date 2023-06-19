def main():
    s = input()
    t = input()
    s = list(s)
    t = list(t)
    for i in range(len(t)):
        if t[i] == '?':
            t[i] = s[i]
    t = ''.join(t)
    for i in range(len(s)-len(t)+1):
        t1 = s[i:i+len(t)]
        flag = True
        for j in range(len(t)):
            if t1[j] != t[j] and t1[j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
