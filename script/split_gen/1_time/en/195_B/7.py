def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 100000000000
    max = 0
    for i in range(A, B + 1):
        if W % i == 0:
            if W // i < min:
                min = W // i
            if W // i > max:
                max = W // i
    if min == 100000000000:
        print("UNSATISFIABLE")
    else:
        print(min, max)
