def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            print('Yes')
            exit()
        s[i], s[i+1] = s[i+1], s[i]
    print('No')
