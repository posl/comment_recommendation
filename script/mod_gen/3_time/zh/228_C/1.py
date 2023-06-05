def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: sum(x), reverse=True)
    for i in range(n):
        p[i].append(i + 1)
    p.sort(key=lambda x: x[3])
    for i in range(n):
        if p[i][3] <= k:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()