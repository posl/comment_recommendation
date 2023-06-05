def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(i) for i in x]
    print(sum(x_abs))
    print(sum([i**2 for i in x_abs])**0.5)
    print(max(x_abs))

if __name__ == '__main__':
    main()