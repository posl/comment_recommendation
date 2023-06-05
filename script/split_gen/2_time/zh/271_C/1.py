def main():
    n, q = map(int, input().split())
    l = []
    a = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    for i in range(q):
        a.append(list(map(int, input().split())))
    for i in range(q):
        print(l[a[i][0]-1][a[i][1]-1])
main()
