def main():
    S = input()
    count = 0
    for i in range(1000):
        s = str(i).zfill(3)
        p = 0
        for c in S:
            if c == '?':
                if p < 3:
                    p += 1
                else:
                    break
            else:
                if c == s[p]:
                    p += 1
                else:
                    break
        else:
            if p == 3:
                count += 1
    print(count % (10**9 + 7))

if __name__ == '__main__':
    main()