def main():
    n = int(input())
    ans = (10**n - 2*(9**n) + 8**n) % (10**9 + 7)
    print(ans)

if __name__ == '__main__':
    main()