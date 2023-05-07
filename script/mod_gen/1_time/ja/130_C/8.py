def area(x, y, w, h):
    return x * y + (w - x) * (h - y)
w, h, x, y = map(int, input().split())
print(area(x, y, w, h), int(area(x, y, w, h) == max(area(x, y, w, h), area(x, 0, w, y), area(0, y, x, h), area(x, 0, w, h - y))))

if __name__ == '__main__':
    area()