def main():
    n = int(input())
    v = list(map(int, input().split()))
    v0 = v[::2]
    v1 = v[1::2]
    v0c = []
    v1c = []
    for i in range(1, max(v)+1):
        v0c.append(v0.count(i))
        v1c.append(v1.count(i))
    if v0c.index(max(v0c)) == v1c.index(max(v1c)):
        if len(v0c) == 1:
            print(n//2)
        else:
            print(n-max(v0c)-max(v1c))
    else:
        print(n-max(v0c)-max(v1c))

if __name__ == '__main__':
    main()