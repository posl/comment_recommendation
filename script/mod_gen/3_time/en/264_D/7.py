def main():
    s = input()
    atcoder = "atcoder"
    res = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            res += 1
    print(res)
main()
