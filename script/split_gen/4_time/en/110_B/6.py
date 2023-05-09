def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort(reverse=True)
    y.sort()
    for i in range(101):
        if x[0] < i <= y[0] and X < i <= Y:
            print('No War')
            return
    print('War')
