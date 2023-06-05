def main():
    n, q = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(q):
        s, t = map(int, input().split())
        print(l[s-1][t-1])
