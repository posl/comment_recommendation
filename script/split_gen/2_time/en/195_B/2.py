def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_orange = 0
    max_orange = 0
    for i in range(1, W+1):
        if A*i <= W <= B*i:
            if min_orange == 0:
                min_orange = i
            max_orange = i
    if min_orange == 0:
        print('UNSATISFIABLE')
    else:
        print(min_orange, max_orange)
