def main():
    k = int(input())
    h = k // 60
    m = k % 60
    if h > 23:
        h = h - 24
    print('{0:02d}:{1:02d}'.format(h,m))

if __name__ == '__main__':
    main()