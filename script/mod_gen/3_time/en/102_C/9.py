def main():
    # input
    N = int(input())
    As = [*map(int, input().split())]
    # compute
    As = [A-i for i, A in enumerate(As, start=1)]
    As.sort()
    if N % 2 == 0:
        b = (As[N//2-1] + As[N//2]) // 2
    else:
        b = As[N//2]
    # output
    print(sum(abs(A-b) for A in As))

if __name__ == '__main__':
    main()