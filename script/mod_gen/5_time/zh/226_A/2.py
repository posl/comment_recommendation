def main():
    x = float(input())
    x *= 1000
    x = int(x + 0.5)
    print(x // 1000)

if __name__ == '__main__':
    main()