def main():
    k = int(input())
    s = input()
    t = input()
    s = s.replace('#','')
    t = t.replace('#','')
    s = list(s)
    t = list(t)
    s = [int(x) for x in s]
    t = [int(x) for x in t]
    s.sort()
    t.sort()
    s.reverse()
    t.reverse()
    s = ''.join(str(x) for x in s)
    t = ''.join(str(x) for x in t)
    s = int(s)
    t = int(t)
    #print(s)
    #print(t)
    #print(s-t)
    if s-t == 0:
        print(0.0)
    else:
        if s-t > 0:
            print(1.0)
        else:
            print(0.0)
