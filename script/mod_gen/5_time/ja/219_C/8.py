def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    x_dict = {}
    for i in range(len(x)):
        x_dict[x[i]] = chr(i+97)
    s_dict = {}
    for i in range(n):
        s_dict[s[i]] = ""
        for j in range(len(s[i])):
            s_dict[s[i]] += x_dict[s[i][j]]
    s_dict = sorted(s_dict.items(), key=lambda x: x[1])
    for i in range(n):
        print(s_dict[i][0])

if __name__ == '__main__':
    main()