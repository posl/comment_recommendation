def main():
    s = input()
    q = int(input())
    for i in range(q):
        t = input()
        if t == "1":
            s = s[::-1]
        else:
            f, c = t.split()[1:]
            if f == "1":
                s = c + s
            else:
                s = s + c
    print(s)

if __name__ == '__main__':
    main()