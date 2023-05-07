def main():
    n = int(input())
    if n <= 54:
        print("AGC"+str(n+1).zfill(3))
    else:
        print("AGC055")

if __name__ == '__main__':
    main()