def main():
    x, k = map(int, input().split())
    for i in range(1, k+1):
        x = round(x, -i)
    print(x)

if __name__ == '__main__':
    main()