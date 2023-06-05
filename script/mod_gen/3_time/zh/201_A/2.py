def main():
    a = input()
    b = a.split(" ")
    c = []
    for i in b:
        c.append(int(i))
    c.sort()
    if c[2] - c[1] == c[1] - c[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()