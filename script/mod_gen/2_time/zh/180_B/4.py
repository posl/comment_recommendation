def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    x_abs = [abs(x[i]) for i in range(n)]
    print(sum(x_abs))
    print(sum([x_abs[i]**2 for i in range(n)])**0.5)
    print(max(x_abs))

if __name__ == '__main__':
    main()