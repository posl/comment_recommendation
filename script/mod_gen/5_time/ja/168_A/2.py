def main():
    n = int(input())
    print("hon" if n%10 in [2,4,5,7,9] else ("pon" if n%10 in [0,1,6,8] else "bon"))

if __name__ == '__main__':
    main()