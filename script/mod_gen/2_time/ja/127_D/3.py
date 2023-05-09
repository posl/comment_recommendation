def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    bc = [list(map(int, input().split())) for _ in range(m)]
    bc.sort(key = lambda x: x[1], reverse = True)
    i = 0
    for b, c in bc:
        for j in range(b):
            if a[i] < c:
                a[i] = c
                i += 1
            else:
                break
            if i >= n:
                break
        if i >= n:
            break
    print(sum(a))

if __name__ == '__main__':
    main()