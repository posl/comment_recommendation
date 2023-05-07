def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i%A != 0 and i%B != 0:
            ans += i
    print(ans)

if __name__ == '__main__':
    main()