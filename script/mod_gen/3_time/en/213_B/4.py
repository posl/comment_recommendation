def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A = sorted(A, key=lambda x: x[0])
    print(A[1][1] + 1)
main()
