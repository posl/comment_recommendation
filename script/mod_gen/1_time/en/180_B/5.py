def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(xi) for xi in x]))
    print(pow(sum([xi**2 for xi in x]), 0.5))
    print(max([abs(xi) for xi in x]))

if __name__ == '__main__':
    main()