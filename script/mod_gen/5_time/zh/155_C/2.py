def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max_count = 0
    max_str = ""
    count = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            count = 1
        if max_count < count:
            max_count = count
            max_str = s[i]
    print(max_str)

if __name__ == '__main__':
    main()