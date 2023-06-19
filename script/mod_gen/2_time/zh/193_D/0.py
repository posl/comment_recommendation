def main():
    k = int(input())
    s = input()
    t = input()
    s = s[:4]
    t = t[:4]
    s = s.replace('#','')
    t = t.replace('#','')
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    s.reverse()
    t.reverse()
    s = ''.join(s)
    t = ''.join(t)
    s = int(s)
    t = int(t)
    s = s / 10 ** k
    t = t / 10 ** k
    print(s)
    print(t)
    prin

if __name__ == '__main__':
    main()