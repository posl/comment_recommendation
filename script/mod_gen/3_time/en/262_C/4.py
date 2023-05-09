def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N+1):
        if A[i] == i:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()