def main():
    s = input()
    min_s = s
    max_s = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s < min_s:
            min_s = s
        if s > max_s:
            max_s = s
    print(min_s)
    print(max_s)
main()
