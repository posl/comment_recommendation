def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_i, a_i = map(int, input().split())
        c.append(c_i)
        a.append(a_i)
    print(c)
    print(a)
