def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(1, N+1):
        if a[i] == i:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()