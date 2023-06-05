def input():
    n = int(raw_input())
    s = []
    p = []
    for i in range(n):
        line = raw_input().split()
        s.append(line[0])
        p.append(line[1])
    return n, s, p

if __name__ == '__main__':
    input()