def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 1000000
    max = 0
    for i in range(1, W+1):
        if A*i <= W and W <= B*i:
            if i <= min:
                min = i
            if i >= max:
                max = i
    if min == 1000000 or max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
