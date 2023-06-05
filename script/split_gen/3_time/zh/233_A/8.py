def main():
    x,y = map(int, input().split())
    print(0 if x >= y else (y - x) // 10)
