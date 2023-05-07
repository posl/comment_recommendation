def main():
    n = int(input())
    s = input()
    i = 0
    while i < n:
        if s[i] == '"':
            i += 1
            while i < n and s[i] != '"':
                i += 1
        elif s[i] == ',':
            s = s[:i] + '.' + s[i+1:]
        i += 1
    print(s)

if __name__ == '__main__':
    main()