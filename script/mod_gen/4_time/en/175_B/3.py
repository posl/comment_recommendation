def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    res += 1
    print(res)

if __name__ == '__main__':
    main()