def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(q):
        s, t = map(int, input().split())
        print(a[s-1][t-1])
main()
