def main():
    N = int(input())
    A = [0] * (2 * N + 1)
    for i in range(N):
        print(i + 1)
        A[int(input()) - 1] = 1
        if A[i] == 1:
            return
    print(N + 1)
main()
