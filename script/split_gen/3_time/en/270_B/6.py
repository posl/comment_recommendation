def main():
    x, y, z = map(int, input().split())
    if y < z:
        print(-1)
        return
    print(abs(x))
