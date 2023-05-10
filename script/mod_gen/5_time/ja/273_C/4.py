def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = 0
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = 1
        elif A[i] != A[i-1]:
            K += 1
            ans[i] = 1
        else:
            ans[i] = ans[i-1] + 1
    for i in range(N):
        print(ans[i])
main()

if __name__ == '__main__':
    main()