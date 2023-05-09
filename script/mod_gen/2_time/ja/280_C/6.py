def main():
    s = input()
    t = input()
    for i in range(len(s)+1):
        if s[:i] + s[i:] == t:
            print(i+1)
            return

if __name__ == '__main__':
    main()