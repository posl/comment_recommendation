def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k]:
                    if a[i] + a[j] > a[k]:
                        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()