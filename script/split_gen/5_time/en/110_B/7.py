def main():
    n, m, x, y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and x < y:
        print("No War")
    else:
        print("War")
