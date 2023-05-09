def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = W // B
    max = W // A
    if min * B <= W <= max * A:
        print(min, max)
    else:
        print("UNSATISFIABLE")
