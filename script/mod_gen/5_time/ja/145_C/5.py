def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    import itertools
    import math
    l = list(itertools.permutations(range(n)))
    total = 0
    for i in range(len(l)):
        for j in range(n-1):
            total += math.sqrt((x[l[i][j]]-x[l[i][j+1]])**2 + (y[l[i][j]]-y[l[i][j+1]])**2)
    print(total/len(l))
main()

if __name__ == '__main__':
    main()