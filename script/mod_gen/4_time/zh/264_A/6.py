def main():
    a = input()
    b = a.split(" ")
    c = int(b[0])
    d = int(b[1])
    e = "atcoder"
    print(e[c-1:d])

if __name__ == '__main__':
    main()