def main():
    N, K = [int(x) for x in input().split()]
    if N % K == 0:
        print(0)
    else:
        print(1)
main()
