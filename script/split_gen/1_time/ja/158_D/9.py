def main():
    S = list(input())
    Q = int(input())
    t = []
    f = []
    c = []
    for _ in range(Q):
        T = input().split()
        t.append(T[0])
        if len(T) == 3:
            f.append(T[1])
            c.append(T[2])
    #print(S)
    #print(Q)
    #print(t)
    #print(f)
    #print(c)
    rev = 0
    for i in range(Q):
        if t[i] == '1':
            rev += 1
        else:
            if (int(f[i]) + rev) % 2 == 0:
                S.append(c[i])
            else:
                S.insert(0, c[i])
    #print(S)
    if rev % 2 == 0:
        print(''.join(S))
    else:
        print(''.join(reversed(S)))
