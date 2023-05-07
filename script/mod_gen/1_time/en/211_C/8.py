def main():
    s = input()
    mod = 10**9 + 7
    # 1. count the number of each letter
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    # 2. calculate the number of ways
    ans = 1
    for i in range(8):
        ans = ans * count[i] % mod
        count[i + 1] -= 1
    print(ans)

if __name__ == '__main__':
    main()