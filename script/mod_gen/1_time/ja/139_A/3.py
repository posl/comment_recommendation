def main():
    s = input()
    t = input()
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    print(count)
    return

if __name__ == '__main__':
    main()