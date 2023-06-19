def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for i in range(1000, 2000, 8):
        dd = {}
        for c in str(i):
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        for c in dd:
            if not c in d or dd[c] > d[c]:
                break
        else:
            print("是")
            break
    else:
        print("否")

if __name__ == '__main__':
    main()