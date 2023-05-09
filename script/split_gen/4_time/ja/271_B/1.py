def main():
    n, q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        print(a[b[i][0]-1][b[i][1]-1])
