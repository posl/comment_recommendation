def main():
    a, b, c = map(int, input().split())
    if b in [a, c]:
        print("没有")
    else:
        print("是")

if __name__ == '__main__':
    main()