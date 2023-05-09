def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans += A[i] - 1
    if ans <= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()