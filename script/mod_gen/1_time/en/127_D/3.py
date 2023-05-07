def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append([b, c])
    bc.sort(key=lambda x: x[1], reverse=True)
    j = 0
    for i in range(n):
        if j >= m:
            break
        if bc[j][1] > a[i]:
            a[i] = bc[j][1]
            bc[j][0] -= 1
            if bc[j][0] == 0:
                j += 1
        else:
            break
    print(sum(a))

if __name__ == '__main__':
    main()