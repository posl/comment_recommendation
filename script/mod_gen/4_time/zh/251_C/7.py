def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        l = input().split()
        s.append(l[0])
        t.append(int(l[1]))
    max_t = max(t)
    max_s = []
    for i in range(n):
        if t[i] == max_t:
            max_s.append(s[i])
    min_s = max_s[0]
    for i in range(len(max_s)):
        if min_s > max_s[i]:
            min_s = max_s[i]
    print(s.index(min_s)+1)

if __name__ == '__main__':
    main()