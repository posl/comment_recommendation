def main():
    s,w = map(int, input().split())
    if s > w:
        print("安全")
    else:
        print("不安全")

if __name__ == '__main__':
    main()