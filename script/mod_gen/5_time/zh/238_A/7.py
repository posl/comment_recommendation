def main():
    import sys
    n = int(sys.stdin.readline())
    if 2**n > n**2:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()