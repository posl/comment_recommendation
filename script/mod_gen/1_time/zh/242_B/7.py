def main():
    s = input()
    ss = sorted(s)
    if len(ss) == 1:
        print(ss[0])
    else:
        if ss[0] == ss[1]:
            print("".join(ss))
        else:
            print(ss[0] + "".join(ss[1:]))

if __name__ == '__main__':
    main()