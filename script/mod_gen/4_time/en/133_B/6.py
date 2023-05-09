def main():
    import sys
    import math
    n, d = map(int, sys.stdin.readline().split())
    x = []
    for i in range(n):
        x.append(list(map(int, sys.stdin.readline().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = 0
            for k in range(d):
                dist += (x[i][k] - x[j][k]) ** 2
            if math.sqrt(dist).is_integer():
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()