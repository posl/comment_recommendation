def main():
    N, M, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.append(X)
    B.append(Y)
    A.sort()
    B.sort()
    if A[-1] < B[0]:
        print('No War')
    else:
        print('War')
main()

if __name__ == '__main__':
    main()