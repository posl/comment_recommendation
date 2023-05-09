def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    b = []
    for i in range(n):
        b.append(tuple(a[i][1::]))
    print(len(set(b)))
main()
