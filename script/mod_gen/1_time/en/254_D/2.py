def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i * j > N:
                break
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans)

if __name__ == '__main__':
    main()