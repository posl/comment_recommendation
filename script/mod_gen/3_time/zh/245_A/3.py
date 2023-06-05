def main():
    a, b, c, d = map(int, input().split())
    if (a * 60 + b) < (c * 60 + d):
        print("青木")
    else:
        print("高桥")

if __name__ == '__main__':
    main()