def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N//2):
        a = A[i]
        b = A[N-1-i]
        if a != b:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()