def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    a.sort()
    for i in range(q):
        count = 0
        for j in range(n):
            if x[i] <= a[j]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()