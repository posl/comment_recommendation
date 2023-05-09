def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        flag = True
        for j in range(N):
            if not (A[j] <= i <= B[j]):
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()