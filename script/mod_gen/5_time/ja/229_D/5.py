def main():
    s = input()
    k = int(input())
    s = s.replace("X", "X.")
    s = s.split(".")
    max_len = 0
    for i in range(len(s)):
        max_len = max(max_len, len(s[i]))
    if len(s) - 1 <= k:
        print(len(s) - 1)
    else:
        print(max_len)

if __name__ == '__main__':
    main()