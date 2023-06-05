def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    count = 0
    max = 0
    for i in range(n):
        count = s.count(s[i])
        if count > max:
            max = count
            result = s[i]
    print(result)

if __name__ == '__main__':
    main()