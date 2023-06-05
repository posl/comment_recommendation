def main():
    X, Y = map(int, input().split())
    print((Y-X%Y)%Y)
