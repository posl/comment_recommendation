def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[len(s)-len(t)+i:] == t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()