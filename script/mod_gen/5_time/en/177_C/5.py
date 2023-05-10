def main():
    N = int(input())
    A_list = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A_list[i] * sum(A_list[i+1:])
    print(ans % (10**9+7))
main()

if __name__ == '__main__':
    main()