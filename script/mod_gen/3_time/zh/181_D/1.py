def main():
    s = input()
    if len(s) < 3:
        print("否")
    else:
        for i in range(100, 1000):
            if i % 8 == 0:
                si = str(i)
                if si[0] in s and si[1] in s and si[2] in s:
                    print("是")
                    exit()
        print("否")

if __name__ == '__main__':
    main()