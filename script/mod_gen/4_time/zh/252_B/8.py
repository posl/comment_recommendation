def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()