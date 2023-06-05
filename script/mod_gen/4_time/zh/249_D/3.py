def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    dic = {}
    for i in range(n):
        if a[i] in dic:
            dic[a[i]] += 1
        else:
            dic[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] == 0:
                if a[i] // a[j] in dic:
                    cnt += dic[a[i] // a[j]]
    print(cnt)

if __name__ == '__main__':
    main()