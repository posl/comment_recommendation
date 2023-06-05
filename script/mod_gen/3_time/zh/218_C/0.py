def problem218_c():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(input()))
    for i in range(n):
        t.append(list(input()))
    if s == t:
        print('Yes')
        return
    for i in range(3):
        t = rotate(t)
        if s == t:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    problem218_c()