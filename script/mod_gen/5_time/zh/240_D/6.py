def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1] + 1
        if A[i] == A[i-1]:
            ans[i] -= 1
            if i-2 >= 0:
                ans[i] += ans[i-2]
            else:
                ans[i] += 1
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()