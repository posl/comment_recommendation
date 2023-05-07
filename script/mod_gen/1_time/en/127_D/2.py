def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            for _ in range(bc[j][0]):
                a[i] = bc[j][1]
                i += 1
                if i >= n:
                    break
            j += 1
        else:
            break
    print(sum(a))

if __name__ == '__main__':
    main()