def main():
    r, D, x2000 = map(int, input().split())
    for i in range(10):
        x2000 = r * x2000 - D
        print(x2000)

if __name__ == '__main__':
    main()