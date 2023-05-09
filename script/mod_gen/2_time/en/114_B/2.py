def main():
    s = input()
    min = 753
    for i in range(len(s) - 2):
        if abs(int(s[i:i+3]) - 753) < min:
            min = abs(int(s[i:i+3]) - 753)
    print(min)
main()

if __name__ == '__main__':
    main()