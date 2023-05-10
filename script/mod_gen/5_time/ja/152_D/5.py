def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            continue
        tmp = i
        while tmp < n+1:
            if tmp % 10 == i // (10 ** len(str(i))-1):
                ans += 1
            tmp *= 10
            tmp += i % 10
    print(ans)

if __name__ == '__main__':
    main()