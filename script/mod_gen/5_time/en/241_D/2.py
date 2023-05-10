def main():
    n = int(input())
    a = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b, reverse=True)[k-1])
        elif q[0] == '3':
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])

if __name__ == '__main__':
    main()