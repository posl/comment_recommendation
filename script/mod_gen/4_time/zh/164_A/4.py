def main():
    s,w = map(int,input().split())
    if w >= s:
        print("不安全")
    else:
        print("安全")

if __name__ == '__main__':
    main()