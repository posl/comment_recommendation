def main():
    n = int(input())
    a = []
    for _ in range(n):
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
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(q[1])
            k = int(q[2])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])

if __name__ == '__main__':
    main()