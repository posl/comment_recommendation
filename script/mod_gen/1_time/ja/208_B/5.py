def main():
    P = int(input())
    coin = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ans = 0
    for c in coin:
        if P >= factorial(c):
            ans += P // factorial(c)
            P = P % factorial(c)
    print(ans)

if __name__ == '__main__':
    main()