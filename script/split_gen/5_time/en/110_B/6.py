def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if X < min(y) and max(x) < Y and max(x) < min(y):
        print("No War")
    else:
        print("War")
