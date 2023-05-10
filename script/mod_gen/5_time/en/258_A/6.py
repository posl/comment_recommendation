def main():
    K = int(input())
    print("{:02d}:{:02d}".format((K//60+21)%24,K%60))

if __name__ == '__main__':
    main()