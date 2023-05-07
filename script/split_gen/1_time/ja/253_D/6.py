def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    sumA = (N // A) * (N // A + 1) // 2 * A
    sumB = (N // B) * (N // B + 1) // 2 * B
    sumAB = (N // (A * B)) * (N // (A * B) + 1) // 2 * (A * B)
    print(sumA + sumB - sumAB)
