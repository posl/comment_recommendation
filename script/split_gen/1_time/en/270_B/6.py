def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(-1)
    elif x < z < y:
        print(-1)
    else:
        print(abs(x - z))
