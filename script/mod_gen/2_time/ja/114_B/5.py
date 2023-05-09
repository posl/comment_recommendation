def main():
    s = input()
    min_diff = 1000
    for i in range(len(s) - 2):
        x = int(s[i:i+3])
        diff = abs(x - 753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
main()

if __name__ == '__main__':
    main()