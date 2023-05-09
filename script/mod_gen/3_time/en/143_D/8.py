def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] < l[j] + l[k]:
                    cnt += 1
                else:
                    break
    print(cnt)

if __name__ == '__main__':
    main()