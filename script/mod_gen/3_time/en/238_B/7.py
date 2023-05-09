def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - a for a in A]
    A = A[::-1]
    A.append(0)
    ans = 0
    for i in range(N + 1):
        ans += min(A[i], A[i + 1])
    print(ans)

if __name__ == '__main__':
    main()