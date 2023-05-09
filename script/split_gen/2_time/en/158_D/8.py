def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = False
    for i in range(q):
        t, *f = input().split()
        if t == '1':
            rev = not rev
        else:
            if rev:
                if f[0] == '1':
                    s.append(f[1])
                else:
                    s.insert(0, f[1])
            else:
                if f[0] == '1':
                    s.insert(0, f[1])
                else:
                    s.append(f[1])
    if rev:
        s.reverse()
    print(''.join(s))
