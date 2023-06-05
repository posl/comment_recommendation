def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    if len(s) == len(t):
        print('No')
        return
    if s[0] != t[0]:
        print('No')
        return
    if s[-1] != t[-1]:
        print('No')
        return
    s = s[1:-1]
    t = t[1:-1]
    if s == t:
        print('Yes')
    else:
        print('No')
main()
