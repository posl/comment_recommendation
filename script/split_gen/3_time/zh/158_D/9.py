def main():
    s = input()
    q = int(input())
    s = list(s)
    flag = True
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            flag = not flag
        else:
            if t[1] == '1':
                if flag:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
            else:
                if flag:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
    if flag:
        print(''.join(s))
    else:
        print(''.join(s[::-1]))
