def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = []
    for i in range(100):
        B.extend(A)
    sum = 0
    k = 0
    for i in range(len(B)):
        sum += B[i]
        k = i
        if sum > X:
            break
    print(k+1)

if __name__ == '__main__':
    main()