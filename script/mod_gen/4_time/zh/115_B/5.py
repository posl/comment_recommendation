def problem115_b():
    n = int(input())
    p = [int(input()) for i in range(n)]
    max = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
    total = 0
    for i in range(n):
        if p[i] == max:
            total += int(max / 2)
        else:
            total += p[i]
    print(total)

if __name__ == '__main__':
    problem115_b()