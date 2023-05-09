def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    s = 0
    for i in range(2 * N):
        s += A[2 * i]
    print(s)
main()
