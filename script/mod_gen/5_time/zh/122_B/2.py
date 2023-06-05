def main():
    s = input()
    max_len = 0
    count = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            count += 1
        else:
            count = 0
        max_len = max(max_len, count)
    print(max_len)
main()
