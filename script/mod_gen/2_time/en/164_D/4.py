def main():
    S = input()
    N = len(S)
    S = S[::-1]
    ans = 0
    d = [0] * 2019
    d[0] = 1
    num = 0
    for i in range(N):
        num += int(S[i]) * pow(10, i, 2019)
        num %= 2019
        ans += d[num]
        d[num] += 1
    print(ans)
    return
main()

if __name__ == '__main__':
    main()