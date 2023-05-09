def main():
    import math
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            len = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if len > max_len:
                max_len = len
    print(max_len)

if __name__ == '__main__':
    main()