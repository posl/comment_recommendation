def main():
    s = input()
    min = s
    max = s
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s < min:
            min = s
        if s > max:
            max = s
    print(min)
    print(max)
main()
