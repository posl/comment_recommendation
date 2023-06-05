def main():
    a,b,c = map(int, input().split())
    if (a <= b and b <= c) or (c <= b and b <= a):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()