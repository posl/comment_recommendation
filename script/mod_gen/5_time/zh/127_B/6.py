def get_next(x, r, D):
    return r * x - D
r, D, x = map(int, input().split())
for i in range(10):
    x = get_next(x, r, D)
    print(x)

if __name__ == '__main__':
    get_next()