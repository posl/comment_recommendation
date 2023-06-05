def check():
    n = input()
    l = []
    for i in range(n):
        s = raw_input()
        l.append(s)
    l = set(l)
    if len(l) == n:
        for i in l:
            if i[0] not in 'HDCS':
                return 'No'
            if i[1] not in 'A23456789TJQK':
                return 'No'
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    check()