def main():
    K = int(input())
    H = K//60
    M = K%60
    print("{:02}:{:02}".format(H+21,M))

if __name__ == '__main__':
    main()