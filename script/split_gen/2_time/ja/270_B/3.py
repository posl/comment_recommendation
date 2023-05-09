def main():
    x, y, z = map(int, input().split())
    if x > 0:
        print(x - y)
    elif x < 0:
        print(-x + y)
    else:
        if y > 0:
            print(y - z)
        elif y < 0:
            print(-y + z)
        else:
            print(z)
