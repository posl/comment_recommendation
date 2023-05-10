def main():
    k = int(input())
    time = 2100
    hour = k // 60
    minute = k % 60
    time = time + hour * 100 + minute
    print("{:04d}".format(time))

if __name__ == '__main__':
    main()