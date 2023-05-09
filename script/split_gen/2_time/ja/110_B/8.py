def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = max(x) + 1
    if z > min(y) or z <= X or z > Y:
        print('War')
    else:
        print('No War')
