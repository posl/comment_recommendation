def main():
    s = input()
    t = input()
    for i in range(len(s)-len(t)+1):
        if t == s[:i] + t + s[i+len(t):]:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()