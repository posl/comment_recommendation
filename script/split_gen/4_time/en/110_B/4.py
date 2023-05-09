def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) >= min(y) or max(x) >= Y or min(y) <= X:
        print('War')
    else:
        print('No War')
