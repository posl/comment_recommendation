def main():
    n = int(input())
    q = []
    for i in range(n):
        q.append(list(map(int, input().split())))
    l = []
    r = []
    for i in range(n):
        if q[i][0] == 1:
            for j in range(q[i][2]):
                r.append(q[i][1])
        else:
            for j in range(q[i][1]):
                l.append(r[0])
                r.pop(0)
            print(sum(l))

if __name__ == '__main__':
    main()