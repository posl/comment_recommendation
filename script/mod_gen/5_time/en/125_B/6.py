def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x_y = 0
    for i in range(n):
        if v[i] > c[i]:
            x_y += v[i] - c[i]
    print(x_y)

if __name__ == '__main__':
    main()