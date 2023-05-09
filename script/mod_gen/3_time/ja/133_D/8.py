def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(A[i] - (sum(A) - A[i]))
        else:
            ans.append(A[i] - (A[i - 1]))
    print(*ans)

if __name__ == '__main__':
    main()