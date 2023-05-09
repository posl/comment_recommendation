def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [j for i in A for j in i]
    A.sort()
    ans = 0
    for i in range(len(A)):
        ans += abs(A[i] - A[len(A)//2])
    print(ans)

if __name__ == '__main__':
    main()