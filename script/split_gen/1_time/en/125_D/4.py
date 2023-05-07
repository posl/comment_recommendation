def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    if N % 2 == 0:
        print(S)
    else:
        print(S - 2 * min(abs(x) for x in A))
main()
