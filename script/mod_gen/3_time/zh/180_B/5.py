def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum([i*i for i in x_abs])**0.5)
    print(max(x_abs))

if __name__ == '__main__':
    main()