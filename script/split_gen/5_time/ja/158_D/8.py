def main():
    s = input()
    q = int(input())
    s = list(s)
    reverse = False
    for i in range(q):
        query = input()
        if query[0] == '1':
            reverse = not reverse
        else:
            t, f, c = query.split()
            if reverse:
                f = '1' if f == '2' else '2'
            if f == '1':
                s.insert(0, c)
            else:
                s.append(c)
    if reverse:
        s = s[::-1]
    print(''.join(s))
