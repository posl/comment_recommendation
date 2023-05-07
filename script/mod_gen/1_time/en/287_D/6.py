def main():
    s = input()
    t = input()
    for x in range(len(t)+1):
        s1 = s[:x]
        s2 = s[len(s)-len(t)+x:]
        if s1.count('?') + s2.count('?') + t.count('?') == len(t) and s1.replace('?','a') + s2.replace('?','a') == t.replace('?','a'):
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()