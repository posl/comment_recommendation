def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += 75 * (n//i)**2
    print(ans)

if __name__ == '__main__':
    main()