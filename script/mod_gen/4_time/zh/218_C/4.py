def read_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(input()))
    for i in range(n):
        t.append(list(input()))
    return n, s, t

if __name__ == '__main__':
    read_input()