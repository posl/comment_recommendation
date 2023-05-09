def main():
    h, m = map(int, input().split())
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    if h == 23:
        h = "00"
    elif m == "00":
        h = str(h+1)
        if len(h) == 1:
            h = "0" + h
    else:
        h = str(h)
    print(h + " " + m)

if __name__ == '__main__':
    main()