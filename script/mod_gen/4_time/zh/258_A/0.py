def main():
    K = int(input())
    H = K // 60
    M = K % 60
    print("{0:02d}:{1:02d}".format(21 + H % 24, M))

if __name__ == '__main__':
    main()