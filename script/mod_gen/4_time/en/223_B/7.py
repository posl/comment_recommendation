def main():
    s = input()
    s = list(s)
    n = len(s)
    s1 = s[1:]
    s1.append(s[0])
    s2 = s[n-1:] + s[:n-1]
    print(min(''.join(s1), ''.join(s2)))
    print(max(''.join(s1), ''.join(s2)))

if __name__ == '__main__':
    main()