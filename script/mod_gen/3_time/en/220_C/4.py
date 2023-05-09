def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #print(N)
    #print(A)
    #print(X)
    #B = []
    #for i in range(10 ** 100):
    #    B.extend(A)
    B = A * (10 ** 100)
    #print(B)
    total = 0
    for i in range(len(B)):
        total += B[i]
        if total > X:
            print(i + 1)
            break

if __name__ == '__main__':
    main()