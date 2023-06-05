def resolve():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(m):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    print(k)
    print(a)
    print("Yes")

if __name__ == '__main__':
    resolve()