def main():
    n, q = map(int, input().split())
    l = [0] * n
    a = []
    for i in range(n):
        l[i] = int(input().split()[0])
        a.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])
