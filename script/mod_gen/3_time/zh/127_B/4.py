def problems127_b():
    r, D, x = map(int, input().split())
    for i in range(10):
        x = r * x - D
        print(x)

if __name__ == '__main__':
    problems127_b()