def main():
    N = int(input().strip())
    ans = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i*j == (int(i**0.5))**2 * (int(j**0.5))**2:
                if i == j:
                    ans += 1
                else:
                    ans += 2
    print(ans)

if __name__ == '__main__':
    main()