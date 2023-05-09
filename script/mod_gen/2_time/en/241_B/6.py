def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = "Yes"
    for i in range(M):
        if B[i] < A[0] or B[i] > A[-1]:
            ans = "No"
            break
        else:
            for j in range(N):
                if A[j] >= B[i]:
                    A.pop(j)
                    N -= 1
                    break
    print(ans)

if __name__ == '__main__':
    main()