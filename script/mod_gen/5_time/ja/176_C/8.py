def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i
    ans = 0
    tmp = 0
    for i in range(N):
        if i == 0:
            tmp = B[i]
        else:
            if tmp > B[i]:
                ans += 1
            else:
                tmp = B[i]
    print(ans)

if __name__ == '__main__':
    main()