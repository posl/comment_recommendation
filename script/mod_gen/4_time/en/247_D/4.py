def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input().split()
        if s[0] == "1":
            if s[1] in d:
                d[s[1]] += int(s[2])
            else:
                d[s[1]] = int(s[2])
        else:
            for i in sorted(d.keys())[:int(s[1])]:
                print(d[i])
                del d[i]

if __name__ == '__main__':
    main()