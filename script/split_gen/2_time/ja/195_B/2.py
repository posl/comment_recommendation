def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 0
    max = 0
    for i in range(1, W + 1):
        if A * i <= W and W <= B * i:
            min = i
            break
    for i in range(1, W + 1):
        if A * i <= W and W <= B * i:
            max = i
    if min == 0 and max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
