def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    ans = T[0]
    for i in range(1,N):
        ans = ans + T[i]
    print(ans)

if __name__ == '__main__':
    main()