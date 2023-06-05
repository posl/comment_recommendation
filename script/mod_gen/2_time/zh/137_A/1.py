def main():
    s = input()
    l = len(s)
    #print(l)
    #print(s)
    #print(s[0])
    #print(s[l-1])
    #print(s[0] == 'R')
    #print(s[l-1] == 'L')
    if s[0] == 'R' and s[l-1] == 'L':
        for i in range(l):
            if s[i] == 'L' and s[i-1] == 'R':
                t = i
                break
        for i in range(l):
            if s[i] == 'L' and s[i+1] == 'R':
                t1 = i
                break
        #print(t)
        #print(t1)
        for i in range(l):
            if i < t:
                if (t - i) % 2 == 0:
                    print(0, end = ' ')
                else:
                    print(1, end = ' ')
            elif i == t:
                print(1, end = ' ')
            elif i > t and i < t1:
                print(2, end = ' ')
            elif i == t1:
                print(1, end = ' ')
            elif i > t1:
                if (i - t1) % 2 == 0:
                    print(1, end = ' ')
                else:
                    print(0, end = ' ')
    elif s[0] == 'R' and s[l-1] == 'R':
        for i in range(l):
            if s[i] == 'L' and s[i-1] == 'R':
                t = i
                break
        for i in range(l):
            if s[i] == 'L' and s[i+1] == 'R':
                t1 = i
                break
        #print(t)
        #print(t1)
        for i in range(l):
            if i < t:
                if (t - i) % 2 == 0:
                    print(0, end = ' ')
                else:
                    print(1, end = ' ')
            elif i == t:
                print(1, end = ' ')
            elif i > t and i < t1:
                print(2, end = ' ')
            elif i == t1:
                print(1, end =

if __name__ == '__main__':
    main()