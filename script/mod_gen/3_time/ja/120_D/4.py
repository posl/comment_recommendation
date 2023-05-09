def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[M-1] = N*(N-1)//2
    for i in range(M-1):
        a, b = AB[i]
        if a > b:
            a, b = b, a
        ans[M-i-2] = ans[M-i-1] - (N-a+1)*(N-b+1)//2
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()