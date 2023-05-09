def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if ans == A[i]:
            ans += 1
        elif ans < A[i]:
            break
    print(ans)
main()

if __name__ == '__main__':
    main()