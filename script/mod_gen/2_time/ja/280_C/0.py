def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] == t[:i] and s[i:] == t[i+1:]:
            print(i+1)
            break

if __name__ == '__main__':
    main()