def main():
    s = input()
    r = 0
    m = 0
    for i in range(3):
        if s[i] == "R":
            r += 1
            if r > m:
                m = r
        else:
            r = 0
    print(m)

if __name__ == '__main__':
    main()