def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            ans = i
            break
    if ans == 0:
        ans = N
    print(ans - 1)

if __name__ == '__main__':
    main()