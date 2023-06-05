def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().split())
    a = list(map(lambda x: list(map(int, x)), a))
    b = []
    for i in range(n):
        if a[i][0] == 1:
            for j in range(a[i][2]):
                b.append(a[i][1])
        else:
            print(sum(b[:a[i][1]]))

if __name__ == '__main__':
    main()