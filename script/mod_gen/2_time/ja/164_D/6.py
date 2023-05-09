def main():
    S = input()
    S = S[::-1]
    mod = 2019
    count = 0
    num = 0
    for i in range(len(S)):
        num += int(S[i]) * pow(10, i, mod)
        num %= mod
        if num == 0:
            count += 1
    for i in range(1, len(S)):
        count += i * (int(S[i]) * pow(10, i-1, mod) % mod == 0)
    print(count)

if __name__ == '__main__':
    main()