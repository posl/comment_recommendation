def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = 0
    max = 0
    for i in range(1, 1001):
        if A * i <= W <= B * i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
