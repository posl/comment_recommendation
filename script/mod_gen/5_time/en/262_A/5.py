def main():
    Y = int(input())
    if Y%4 == 0:
        print(Y+2)
    else:
        print(Y+4-Y%4)

if __name__ == '__main__':
    main()