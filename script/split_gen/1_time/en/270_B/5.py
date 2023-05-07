def main():
    x, y, z = map(int, input().split())
    if x < y:
        if x < z < y:
            print(y - x)
        else:
            print(-1)
    elif x > y:
        if y < z < x:
            print(x - y)
        else:
            print(-1)
    else:
        print(-1)
