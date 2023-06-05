def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif s[i] == s[i-1]:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif s[i] == s[i-1]:
            count += 1
        else:
            if count == max:
                print(s[i-1])
            count = 1
    if count == max:
        print(s[n-1])

if __name__ == '__main__':
    main()