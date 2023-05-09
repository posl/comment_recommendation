def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(map(lambda x: x**2, x_abs))**0.5)
    print(max(x_abs))

if __name__ == '__main__':
    main()