def main():
    N, M, X, Y = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print('No War')
    else:
        print('War')
