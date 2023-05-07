def main():
    n, q = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(q):
        s, t = [int(x) for x in input().split()]
        print(a[s-1][t])
