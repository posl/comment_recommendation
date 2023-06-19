def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x0, y0 = map(int, input().split())
        x.append(x0)
        y.append(y0)
    import itertools
    import math
    sum = 0
    for i in itertools.permutations(range(n)):
        for j in range(n-1):
            sum += math.sqrt((x[i[j]]-x[i[j+1]])**2 + (y[i[j]]-y[i[j+1]])**2)
    print(sum/math.factorial(n))

if __name__ == '__main__':
    main()