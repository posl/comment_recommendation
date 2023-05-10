def solve():
    import sys
    readline = sys.stdin.buffer.readline
    s = readline().rstrip().decode('utf-8')
    for i in range(112, 1000, 8):
        if not len(set(str(i))) <= len(set(s)) - s.count('0'):
            continue
        c = 0
        for j in range(3):
            if str(i).count(str(j)) > s.count(str(j)):
                break
            c += 1
        if c == 3:
            print('Yes')
            exit()
    print('No')
    exit()
