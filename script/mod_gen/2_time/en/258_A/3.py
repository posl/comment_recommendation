def main():
    K = int(input())
    print("{0:02d}:{1:02d}".format((K+2100)//100, (K+2100)%100))

if __name__ == '__main__':
    main()