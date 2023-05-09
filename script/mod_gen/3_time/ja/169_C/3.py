def main():
    a,b = input().split()
    a = int(a)
    b = float(b)
    b = int(b * 100)
    print(a * b // 100)
main()

if __name__ == '__main__':
    main()