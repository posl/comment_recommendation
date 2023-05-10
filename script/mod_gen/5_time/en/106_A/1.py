def area(a, b):
    return a*b - (a+b-1)
a, b = map(int, input().split())
print(area(a, b))

if __name__ == '__main__':
    area()