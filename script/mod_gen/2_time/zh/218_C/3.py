def get_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    return n, s, t

if __name__ == '__main__':
    get_input()