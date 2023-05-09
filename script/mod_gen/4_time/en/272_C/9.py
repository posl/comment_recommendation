def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 1000001
    for i in range(n):
        b[a[i]] += 1
    if b[0] > 1:
        print(0)
        return
    for i in range(1, 1000001):
        if b[i] > 1:
            print(i * 2)
            return
    for i in range(1, 1000001):
        if b[i] > 0:
            for j in range(i + i, 1000001, i):
                if b[j] > 0:
                    print(j)
                    return
    print(-1)
    return

if __name__ == '__main__':
    main()