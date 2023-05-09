def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = "Yes"
    for i in range(N):
        if A[i] * B[i] != 0:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()