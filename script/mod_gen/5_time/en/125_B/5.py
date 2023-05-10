def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x_y = [v[i] - c[i] for i in range(n)]
    print(sum([x_y[i] for i in range(n) if x_y[i] > 0]))

if __name__ == '__main__':
    main()