def main():
    k = int(input())
    if k == 1:
        print(2)
        return
    k -= 1
    n = 2
    while True:
        if n == 2:
            k -= 1
            if k == 0:
                print(2)
                return
        else:
            k -= (3 ** (n - 1))
            if k < 0:
                k += (3 ** (n - 1))
                break
        n += 1
    # print(n, k)
    ans = [2] * n
    for i in range(n):
        if k >= (3 ** (n - i - 1)):
            ans[i] = 0
            k -= (3 ** (n - i - 1))
        elif k >= (3 ** (n - i - 1)) // 2:
            ans[i] = 2
            k -= (3 ** (n - i - 1)) // 2
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()