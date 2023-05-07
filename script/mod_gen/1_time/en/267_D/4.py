def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, M+1):
        ans += i * max(A)
        A.remove(max(A))
    print(ans)

if __name__ == '__main__':
    main()