def main():
    s = input()
    if '0' in s:
        print('Yes')
        return
    if len(s) < 3:
        print('No')
        return
    l = []
    for i in range(len(s)):
        l.append(int(s[i]))
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if (l[i]*100 + l[j]*10 + l[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')
