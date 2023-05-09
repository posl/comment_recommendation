def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = W // B
    max = W // A
    if A * max <= W <= B * max:
        print(min, max)
    else:
        print("UNSATISFIABLE")
