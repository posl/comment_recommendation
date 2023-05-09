def main():
    n = int(input())
    ans = 0
    for i in range(n+1):
        if i % 2 == 1:
            ans += 1
    print(ans/n)

if __name__ == '__main__':
    main()