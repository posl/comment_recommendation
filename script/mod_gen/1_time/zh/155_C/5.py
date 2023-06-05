def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    count = 1
    max = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count == max:
                print(s[i])
            count = 1
    if count == max:
        print(s[n-1])

if __name__ == '__main__':
    main()