def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    print(sum([abs(x[i]) for i in range(n)]))
    print(sum([x[i]**2 for i in range(n)])**0.5)
    print(max([abs(x[i]) for i in range(n)]))

if __name__ == '__main__':
    main()