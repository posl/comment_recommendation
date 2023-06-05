def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(x[i]) for i in range(n)]
    print(sum(x))
    print(sum([x[i]*x[i] for i in range(n)])**0.5)
    print(max(x))

if __name__ == '__main__':
    main()