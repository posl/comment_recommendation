def main():
    s = input()
    t = input()
    l = len(t)
    for i in range(len(s)-l+1):
        temp = s[i:i+l]
        for j in range(l):
            if temp[j] == '?':
                temp = temp[:j] + t[j] + temp[j+1:]
        if temp == t:
            print('Yes')
        else:
            print('No')
