def main():
    s = input()
    l = len(s)
    if l % 2 == 0:
        print(sum(s[i] != s[l-1-i] for i in range(l//2)))
    else:
        print(sum(s[i] != s[l-1-i] for i in range(l//2)) + 1)
main()
