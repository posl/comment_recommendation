def main():
    # input
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # output
    print(min(K-A[-1]+A[0], A[-1]-A[0]))
main()
