def main():
    s = input()
    min = 1000
    for i in range(len(s) - 2):
        n = int(s[i:i+3])
        if abs(753 - n) < min:
            min = abs(753 - n)
    print(min)

if __name__ == '__main__':
    main()