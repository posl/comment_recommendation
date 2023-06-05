def main():
    s = input()
    q = int(input())
    s = list(s)
    rev = 0
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = 1 - rev
        else:
            if t[1] == '1':
                if rev == 0:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
            else:
                if rev == 0:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
    if rev == 1:
        s.reverse()
    print(''.join(s))
