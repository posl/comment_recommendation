def problems099_b():
    a, b = map(int, input().split())
    total = 0
    for i in range(1, b - a):
        total += i
    print(total - a)

if __name__ == '__main__':
    problems099_b()