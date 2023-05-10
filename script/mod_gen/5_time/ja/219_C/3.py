def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    x = list(x)
    x.sort()
    x_dict = {}
    for i in range(26):
        x_dict[x[i]] = chr(i + 97)
    for i in range(n):
        s[i] = [x_dict[j] for j in s[i]]
        s[i] = "".join(s[i])
    s.sort()
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()