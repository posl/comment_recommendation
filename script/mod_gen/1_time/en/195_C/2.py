def main():
    N = int(input())
    N = N + 1
    N = str(N)
    N = N[::-1]
    ans = 0
    for i in range(len(N)):
        if i % 3 == 2:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()