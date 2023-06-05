def main():
    A, B, C, D, E, F, X = map(int, input().split())
    sumA = 0
    sumB = 0
    for i in range(X):
        if (i % (A + B)) < A:
            sumA += 1
        if (i % (D + E)) < D:
            sumB += 1
        if sumA > sumB:
            print("高桥")
            break
        elif sumA < sumB:
            print("青木")
            break
    else:
        print("画")
