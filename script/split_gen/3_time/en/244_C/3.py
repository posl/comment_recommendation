def main():
    N = int(input())
    A = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 1):
        print(i)
        a = int(input())
        if a == 0:
            break
        A[a] = 1
        if sum(A) == 2 * N:
            break
main()
