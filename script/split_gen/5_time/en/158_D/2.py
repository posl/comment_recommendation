def main():
    s = input()
    s = list(s)
    q = int(input())
    reverse = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            f = int(t[1])
            c = t[2]
            if f == 1:
                if reverse:
                    s.append(c)
                else:
                    s.insert(0, c)
            else:
                if reverse:
                    s.insert(0, c)
                else:
                    s.append(c)
    if reverse:
        s.reverse()
    print(''.join(s))
