def main():
    s = input()
    if len(s) == 1:
        if int(s) % 8 == 0:
            print("是")
        else:
            print("否")
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print("是")
        else:
            print("否")
    else:
        for i in range(112, 1000, 8):
            if "".join(sorted(s)).count(str(i)[0]) >= str(i).count(str(i)[0]):
                if "".join(sorted(s)).count(str(i)[1]) >= str(i).count(str(i)[1]):
                    if "".join(sorted(s)).count(str(i)[2]) >= str(i).count(str(i)[2]):
                        print("是")
                        return
        print("否")

if __name__ == '__main__':
    main()