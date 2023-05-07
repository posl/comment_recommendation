def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    print(sum([abs(x[i]-x[n//2]) for i in range(n)]))

if __name__ == '__main__':
    main()