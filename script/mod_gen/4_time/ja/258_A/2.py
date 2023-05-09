def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02d}:{:02d}".format(h+21 if h+21 < 24 else h+21-24, m))
    return

if __name__ == '__main__':
    main()