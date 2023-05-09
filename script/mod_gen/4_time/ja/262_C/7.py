def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] > i+1:
            continue
        for j in range(i+1, N):
            if a[i] == i+1 and a[j] == j+1:
                ans += 1
            elif a[i] == j+1 and a[j] == i+1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()