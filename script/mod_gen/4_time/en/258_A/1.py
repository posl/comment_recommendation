def main():
    k = int(input())
    h = k // 60
    m = k % 60
    print("{:02}:{:02}".format(21+h,m))

if __name__ == '__main__':
    main()