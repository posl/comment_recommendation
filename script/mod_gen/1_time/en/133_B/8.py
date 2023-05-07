def main():
    n, d = map(int, input().split())
    xs = [list(map(int, input().split())) for _ in range(n)]
    def distance(x, y):
        return sum((x_i - y_i) ** 2 for x_i, y_i in zip(x, y)) ** 0.5
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if distance(xs[i], xs[j]).is_integer():
                result += 1
    print(result)

if __name__ == '__main__':
    main()