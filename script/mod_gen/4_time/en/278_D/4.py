def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    for i in range(q):
        b.append(list(map(int, input().split())))
    for i in range(q):
        if b[i][0] == 1:
            for j in range(n):
                a[j] = b[i][1]
        elif b[i][0] == 2:
            a[b[i][1] - 1] += b[i][2]
        elif b[i][0] == 3:
            print(a[b[i][1] - 1])

if __name__ == '__main__':
    main()