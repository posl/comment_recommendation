def main():
    k = int(input())
    print("{:02d}:{:02d}".format((k+20)//60, (k+20)%60))
    return

if __name__ == '__main__':
    main()