def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min = 1
    max = 10**9
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]
    if min > max:
        print(0)
    else:
        print(max - min + 1)

if __name__ == '__main__':
    main()