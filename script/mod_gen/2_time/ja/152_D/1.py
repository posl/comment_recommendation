def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i < 10:
            ans += 1
        elif i < 100:
            ans += 9
        elif i < 1000:
            ans += 90
        elif i < 10000:
            ans += 900
        elif i < 100000:
            ans += 9000
        else:
            ans += 90000
    print(ans)

if __name__ == '__main__':
    main()