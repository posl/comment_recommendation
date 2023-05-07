def main():
    X, Y = map(int, input().split())
    print(max(0, -(-Y//10) - X//10))
