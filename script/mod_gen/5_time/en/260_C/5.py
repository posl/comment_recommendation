def problem():
    n, x, y = map(int, input().split())
    return (n-1)*y + x
print(problem())

if __name__ == '__main__':
    problem()