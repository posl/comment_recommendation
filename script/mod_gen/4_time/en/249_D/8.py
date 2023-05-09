def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i]%A[j] == 0:
                ans += A.count(A[i]//A[j])
    print(ans)

if __name__ == '__main__':
    main()