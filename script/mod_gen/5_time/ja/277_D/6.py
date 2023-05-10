def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(M)
    ans = 0
    for i in range(N):
        if A[i] == A[i+1]:
            ans += 1
        else:
            ans += A[i+1] - A[i] - 1
    print(ans)

if __name__ == '__main__':
    main()