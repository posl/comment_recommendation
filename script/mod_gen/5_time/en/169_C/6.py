def main():
    a, b = map(float, input().split())
    print(int(a * (b * 100) // 100))

if __name__ == '__main__':
    main()