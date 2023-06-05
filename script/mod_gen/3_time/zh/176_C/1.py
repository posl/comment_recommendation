def main():
    N = int(input())
    A = list(map(int,input().split()))
    max_h = 0
    ans = 0
    for i in range(N):
        if max_h <= A[i]:
            ans += max_h - A[i]
            max_h = A[i]
        else:
            max_h = A[i]
    print(ans)

if __name__ == '__main__':
    main()