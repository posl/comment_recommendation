def main():
    n = int(input())
    ans = 0
    for i in range(3, len(str(n))+1, 3):
        ans += (n - 10**(i-1) + 1)
    print(ans)

if __name__ == '__main__':
    main()