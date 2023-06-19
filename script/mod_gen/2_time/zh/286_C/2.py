def main():
    input_line = input()
    input_line = input_line.split()
    n = int(input_line[0])
    a = int(input_line[1])
    b = int(input_line[2])
    s = input()
    s = list(s)
    s.reverse()
    count = 0
    for i in range(n):
        if s[i] == s[n-i-1]:
            continue
        elif s[i] != s[n-i-1]:
            if s[i] == 'a':
                count += a
                s[i] = s[n-i-1]
            elif s[i] == 'b':
                count += b
                s[n-i-1] = s[i]
            elif s[n-i-1] == 'a':
                count += a
                s[n-i-1] = s[i]
            elif s[n-i-1] == 'b':
                count += b
                s[i] = s[n-i-1]
    print(count)

if __name__ == '__main__':
    main()