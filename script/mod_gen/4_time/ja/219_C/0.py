def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(26):
        dic[x[i]] = chr(ord("a") + i)
    s.sort(key=lambda x: "".join([dic[c] for c in x]))
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()