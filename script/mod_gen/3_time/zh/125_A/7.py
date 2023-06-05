def problem125_a():
    a, b, t = map(int, input().split())
    count = 0
    for i in range(1, t+1):
        if i % a == 0:
            count += b
    print(count)

if __name__ == '__main__':
    problem125_a()