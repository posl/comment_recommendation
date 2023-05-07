def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    num = 1
    ans = []
    for i in range(N):
        if A[i] == A[i-1]:
            num += 1
        else:
            ans.append(num)
            num = 1
    ans.appen

if __name__ == '__main__':
    main()