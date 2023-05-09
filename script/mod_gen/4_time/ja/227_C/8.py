def main():
    n = int(input())
    ans = 0
    for a in range(1, n+1):
        tmp = n // a
        for b in range(a, tmp+1):
            tmp2 = tmp // b
            if tmp2 >= b:
                ans += tmp2 - b + 1
    print(ans)

if __name__ == '__main__':
    main()