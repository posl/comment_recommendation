def main():
    N = int(input())
    X,Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(X)
    #print(Y)
    #print(N)
    total = 0
    for i in range(N):
        total += A[i] + B[i]
    #print(total)
    if total < X + Y:
        print(-1)
    else:
        count = 0
        while X > 0 or Y > 0:
            if X > 0:
                max = 0
                max_index = 0
                for i in range(N):
                    if A[i] > max:
                        max = A[i]
                        max_index = i
                A[max_index] = -1
                count += 1
                X -= max
            if Y > 0:
                max = 0
                max_index = 0
                for i in range(N):
                    if B[i] > max:
                        max = B[i]
                        max_index = i
                B[max_index] = -1
                count += 1
                Y -= max
        print(count)
main()

if __name__ == '__main__':
    main()