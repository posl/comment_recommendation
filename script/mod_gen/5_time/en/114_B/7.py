def main():
    s = input()
    x = int(s)
    min = 10**10
    for i in range(0, len(s)-2):
        t = int(s[i:i+3])
        if abs(t-753) < min:
            min = abs(t-753)
    print(min)

if __name__ == '__main__':
    main()