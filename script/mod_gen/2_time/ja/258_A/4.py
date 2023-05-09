def main():
    K = int(input())
    h = K // 60
    m = K % 60
    print("{0:02d}:{1:02d}".format(h+21,m))

if __name__ == '__main__':
    main()