def main():
    n = int(input())
    a = []
    for i in range(n):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a.append(q[1])
        elif q[0] == 2:
            if len(a) < q[2]:
                print(-1)
            else:
                b = sorted(a)
                print(b[-q[2]])
        elif q[0] == 3:
            if len(a) < q[2]:
                print(-1)
            else:
                b = sorted(a)
                print(b[q[2]-1])

if __name__ == '__main__':
    main()