def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')
main()
