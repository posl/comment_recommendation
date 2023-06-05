def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    k.sort()
    count = 0
    for i in range(q):
        while a[count] <= k[i]:
            count += 1
        print(k[i] + count)

if __name__ == '__main__':
    main()