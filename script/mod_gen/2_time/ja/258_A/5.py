def main():
    k = int(input())
    hh = 21 + k // 60
    mm = k % 60
    print("{:02}:{:02}".format(hh, mm))

if __name__ == '__main__':
    main()