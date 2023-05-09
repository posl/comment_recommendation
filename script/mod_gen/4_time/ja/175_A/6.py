def main():
    s = input()
    r = 0
    c = 0
    for i in range(3):
        if s[i] == "R":
            c += 1
            if c > r:
                r = c
        else:
            c = 0
    print(r)

if __name__ == '__main__':
    main()