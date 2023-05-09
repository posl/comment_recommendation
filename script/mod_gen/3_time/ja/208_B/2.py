def main():
    P = int(input())
    ans = 0
    for i in range(10, 0, -1):
        ans += P // math.factorial(i)
        P %= math.factorial(i)
    print(ans)

if __name__ == '__main__':
    main()