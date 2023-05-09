def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1:])
    cnt = 1
    for i in range(1, n):
        if l[i] != l[i - 1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()