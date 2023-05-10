def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    s_count = [0] * n
    for i in range(n):
        s_count[i] = s.count(s[i])
    max_s_count = max(s_count)
    for i in range(n):
        if s_count[i] == max_s_count:
            print(s[i])

if __name__ == '__main__':
    main()