def main():
    s, w = map(int, input().split())
    print("安全" if s > w else "不安全")

if __name__ == '__main__':
    main()