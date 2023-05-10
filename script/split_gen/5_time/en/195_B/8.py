def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = int(W / B)
    max = int(W / A)
    if min == max:
        print(min, max)
    elif min < max:
        print(min, max)
    else:
        print("UNSATISFIABLE")
