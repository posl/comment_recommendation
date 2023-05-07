def main():
    K = int(input())
    n = 0
    while True:
        n += 1
        if 2 ** n > K:
            break
    #print(n)
    ans = ""
    for i in range(n-1, -1, -1):
        if K >= 2 ** i:
            ans += "2"
            K -= 2 ** i
        else:
            ans += "0"
    print(ans)

if __name__ == '__main__':
    main()