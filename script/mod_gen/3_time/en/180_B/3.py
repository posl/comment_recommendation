def main():
    N = int(input())
    x = list(map(int,input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**(1/2))
    print(max([abs(i) for i in x]))

if __name__ == '__main__':
    main()