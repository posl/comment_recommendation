def main():
    N = int(input())
    ans = 1
    for i in range(1, N+1):
        ans *= i
    print(ans)

if __name__ == '__main__':
    main()