def main():
    import math
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(N)]))
    print(sum([x[i]*x[i] for i in range(N)])**(1/2))
    print(max([abs(x[i]) for i in range(N)]))

if __name__ == '__main__':
    main()