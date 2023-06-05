def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        sum = 0
        for j in range(i, N):
            sum += j
            if sum == N:
                ans += 1
                break
            elif sum > N:
                break
    print(ans)

if __name__ == '__main__':
    main()