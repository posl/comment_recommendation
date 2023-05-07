def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s.count(s[i]) != t.count(t[i]):
            print('No')
            exit()
    print('Yes')
