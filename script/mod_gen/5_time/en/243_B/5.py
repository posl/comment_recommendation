def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == b[i]:
            cnt += 1
    print(cnt)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()