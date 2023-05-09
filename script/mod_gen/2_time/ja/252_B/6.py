def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    if maxA in A:
        maxA_index = A.index(maxA)
    else:
        maxA_index = -1
    if maxA_index + 1 in B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()