def main():
    x, y, z = map(int, input().split())
    if y < z:
        print(-1)
    else:
        print(abs(x))
