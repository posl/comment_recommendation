def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N and i*j == int(i**0.5)**2 * int(j**0.5)**2:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()