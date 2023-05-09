def main():
    N = int(input())
    X = list(map(int, input().split()))
    print(sum([abs(x) for x in X]))
    print(sum([abs(x)**2 for x in X])**(1/2))
    print(max([abs(x) for x in X]))

if __name__ == '__main__':
    main()