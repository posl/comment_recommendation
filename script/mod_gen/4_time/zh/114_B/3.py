def main():
    s = input()
    min_diff = 1000
    for i in range(len(s)-2):
        diff = abs(int(s[i:i+3])-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == '__main__':
    main()