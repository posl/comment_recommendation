def main():
    n,x,t = map(int, input().split())
    print(((n + x - 1) // x) * t)
    return