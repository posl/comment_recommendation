def main():
    s = input()
    x = 753
    for i in range(len(s) - 2):
        if abs(int(s[i:i+3]) - 753) < x:
            x = abs(int(s[i:i+3]) - 753)
    print(x)

if __name__ == '__main__':
    main()