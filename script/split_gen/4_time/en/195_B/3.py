def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = (W // B) + 1
    max = W // A
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)
