def main():
    r, D, x_2000 = map(int, input().split())
    for i in range(10):
        x = r * x_2000 - D
        print(x)
        x_2000 = x

if __name__ == '__main__':
    main()