def main():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        j = 0
        while j < n:
            if a[j] >= x[i]:
                break
            j += 1
        print(n - j)

if __name__ == '__main__':
    main()