def main():
    import sys
    import numpy as np
    input = sys.stdin.readline
    N = int(input())
    A = [int(x) for x in input().split()]
    A = np.array(A)
    A = np.sort(A)
    B = np.bincount(A)
    for i in range(1, N+1):
        print(B[i])

if __name__ == '__main__':
    main()