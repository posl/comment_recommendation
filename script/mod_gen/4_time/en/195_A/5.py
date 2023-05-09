def main():
    m, h = map(int, input().split())
    print("Yes") if h % m == 0 else print("No")

if __name__ == '__main__':
    main()