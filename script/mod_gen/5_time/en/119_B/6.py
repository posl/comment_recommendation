def problems119_b():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            sum += int(x)
        else:
            sum += float(x) * 380000.0
    print(sum)

if __name__ == '__main__':
    problems119_b()