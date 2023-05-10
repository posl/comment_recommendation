def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    count = 0
    for i in range(1, m+1):
        for j in range(n):
            if i in a[j][1:]:
                if j == n-1:
                    count += 1
                    break
                else:
                    continue
            else:
                break
    print(count)

if __name__ == '__main__':
    main()