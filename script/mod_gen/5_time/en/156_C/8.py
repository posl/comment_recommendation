def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    minx = min(x)
    maxx = max(x)
    minsum = 1000000000000000
    for i in range(minx, maxx+1):
        sumpow = 0
        for j in x:
            sumpow += (j-i)**2
        if minsum > sumpow:
            minsum = sumpow
    print(minsum)

if __name__ == '__main__':
    main()