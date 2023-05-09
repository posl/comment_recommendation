def main():
    x = [0] * 4
    y = [0] * 4
    for i in range(4):
        x[i], y[i] = map(int, input().split())
    ans = "Yes"
    for i in range(4):
        if (x[i] - x[(i + 1) % 4]) * (y[(i + 2) % 4] - y[(i + 1) % 4]) - (x[(i + 2) % 4] - x[(i + 1) % 4]) * (y[i] - y[(i + 1) % 4]) > 0:
            ans = "No"
            break
    print(ans)

if __name__ == '__main__':
    main()