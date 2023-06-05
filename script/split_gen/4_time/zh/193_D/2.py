def main():
    n = int(input())
    s = input()
    t = input()
    s = s[:4]
    t = t[:4]
    s = s.replace('#','')
    t = t.replace('#','')
    s = list(map(int,s))
    t = list(map(int,t))
    s.sort()
    t.sort()
    s.reverse()
    t.reverse()
    s = ''.join(map(str,s))
    t = ''.join(map(str,t))
    s = int(s)
    t = int(t)
    if s > t:
        print(1)
        return
    elif s == t:
        print(0.5)
        return
    else:
        print(0)
        return
