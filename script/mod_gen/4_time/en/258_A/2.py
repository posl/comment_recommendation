def main():
    k = int(input())
    h = 21
    m = 0
    if k <= 59:
        m = k
    else:
        h += k // 60
        m = k % 60
    print(str(h).zfill(2) + ":" + str(m).zfill(2))

if __name__ == '__main__':
    main()