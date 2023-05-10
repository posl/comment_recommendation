def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if a[i] < i+1:
            continue
        for j in range(i+1, N):
            if a[i] == j+1 and a[j] == i+1:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()