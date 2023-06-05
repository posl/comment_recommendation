def main():
    str = input()
    strlist = str.split()
    s = int(strlist[0])
    w = int(strlist[1])
    if s > w:
        print("安全")
    else:
        print("不安全")

if __name__ == '__main__':
    main()