def calculate(r, D, x):
    return r * x - D
r, D, x = map(int, input().split())
for i in range(10):
    x = calculate(r, D, x)
    print(x)

if __name__ == '__main__':
    calculate()