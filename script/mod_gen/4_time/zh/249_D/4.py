def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] % a[j] == 0:
                for k in range(j+1, n):
                    if a[j] % a[k] == 0:
                        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()