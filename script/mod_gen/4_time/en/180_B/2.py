def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(x[i]) for i in range(N)]
    print(sum(x_abs))
    print(sum([x_abs[i]**2 for i in range(N)])**(1/2))
    print(max(x_abs))

if __name__ == '__main__':
    main()