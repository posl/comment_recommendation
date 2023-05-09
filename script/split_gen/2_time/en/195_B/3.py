def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_orange = 10**9
    max_orange = 0
    for i in range(1, 1001):
        if A * i <= W <= B * i:
            min_orange = min(min_orange, i)
            max_orange = max(max_orange, i)
    if min_orange == 10**9:
        print('UNSATISFIABLE')
    else:
        print(min_orange, max_orange)
