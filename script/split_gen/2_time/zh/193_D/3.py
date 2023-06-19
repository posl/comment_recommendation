def main():
    k = int(input())
    s = input()
    t = input()
    s1 = s[:4]
    s2 = s[4]
    t1 = t[:4]
    t2 = t[4]
    #print(k, s1, s2, t1, t2)
    # print(s1)
    # print(s2)
    # print(t1)
    # print(t2)
    s1 = list(map(int, s1))
    t1 = list(map(int, t1))
    #print(s1)
    #print(t1)
    s1.sort()
    t1.sort()
    #print(s1)
    #print(t1)
    s1.reverse()
    t1.reverse()
    #print(s1)
    #print(t1)
    s1 = list(map(str, s1))
    t1 = list(map(str, t1))
    #print(s1)
    #print(t1)
    s1 = ''.join(s1)
    t1 = ''.join(t1)
    #print(s1)
    #print(t1)
    s1 = int(s1)
    t1 = int(t1)
    #print(s1)
    #print(t1)
    #print(s2)
    #print(t2)
    s2 = int(s2)
    t2 = int(t2)
    #print(s2)
    #print(t2)
    s1 = s1 * 10000 + s2
    t1 = t1 * 10000 + t2
    #print(s1)
    #print(t1)
    s1 = s1 / 10000
    t1 = t1 / 10000
    #print(s1)
    #print(t1)
    s1 = s1 * 100000
    t1 = t1 * 100000
    #print(s1)
    #print(t1)
    s1 = int(s1)
    t1 = int(t1)
    #print(s1)
    #print(t1)
    if s1 > t1:
        print(1)
    else:
        print(0)
