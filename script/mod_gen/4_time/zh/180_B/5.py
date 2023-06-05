def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(i**2 for i in x_abs)**(1/2))
    print(max(x_abs))

if __name__ == '__main__':
    main()