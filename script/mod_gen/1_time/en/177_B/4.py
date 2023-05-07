def main():
    s = input()
    t = input()
    min_change = 1001
    for i in range(len(s) - len(t) + 1):
        change = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                change += 1
        min_change = min(min_change, change)
    print(min_change)
main()

if __name__ == '__main__':
    main()