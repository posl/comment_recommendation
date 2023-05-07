def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(0, N):
        for j in range(i, N):
            for k in range(j, N):
                if (A[i] / A[j]) == A[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()