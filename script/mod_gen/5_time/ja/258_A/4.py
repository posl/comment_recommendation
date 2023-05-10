def main():
    k = int(input())
    h = k // 60
    m = k - h * 60
    print("{0:02d}:{1:02d}".format(h + 21, m))
    return

if __name__ == '__main__':
    main()