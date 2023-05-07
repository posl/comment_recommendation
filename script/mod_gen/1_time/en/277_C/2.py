def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print(maxA)
    else:
        print(maxB)

if __name__ == '__main__':
    main()