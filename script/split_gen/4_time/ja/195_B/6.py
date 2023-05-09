def main():
    A, B, W = map(int, input().split())
    max = int(W * 1000 / A)
    min = int(W * 1000 / B)
    if min == max:
        print("UNSATISFIABLE")
    else:
        print(min, max)
