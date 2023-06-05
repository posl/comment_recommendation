def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("是")
        else:
            print("否")
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("是")
        else:
            print("否")
    else:
        a = [0] * 10
        for i in s:
            a[int(i)] += 1
        for i in range(112, 1000, 8):
            b = [0] * 10
            for j in str(i):
                b[int(j)] += 1
            for k in range(0, 10):
                if b[k] > a[k]:
                    break
                elif k == 9:
                    print("是")
                    exit()
        print("否")

if __name__ == '__main__':
    main()