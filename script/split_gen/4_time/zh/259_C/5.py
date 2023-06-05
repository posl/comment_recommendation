def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    if len(s) >= len(t):
        print('No')
        exit()
    s1 = ''
    index = 0
    for i in range(len(t)):
        if index < len(s):
            if s[index] == t[i]:
                s1 += s[index]
                index += 1
            else:
                s1 += t[i]
        else:
            s1 += t[i]
    if s1 == t:
        print('Yes')
    else:
        print('No')
