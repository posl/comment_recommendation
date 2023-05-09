def main():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(A)):
        ans += abs(A[i] - A[i-1])
    print(ans)

if __name__ == '__main__':
    main()