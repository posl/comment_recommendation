def main():
    s = input()
    q = int(input())
    s = list(s)
    reverse = False
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            reverse = not reverse
        else:
            if t[1] == '1':
                if reverse:
                    s.append(t[2])
                else:
                    s.insert(0, t[2])
            else:
                if reverse:
                    s.insert(0, t[2])
                else:
                    s.append(t[2])
    if reverse:
        s.reverse()
    print(''.join(s))
