def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #C = [0] * (10 ** 9 + 2)
    C = [0] * (10 ** 9 + 2)
    for i in range(N):
        #C[A[i]] += 1
        C[A[i]] += 1
        #C[A[i] + B[i]] -= 1
        C[A[i] + B[i]] -= 1
    #print(C)
    for i in range(10 ** 9 + 1):
        C[i + 1] += C[i]
    #print(C)
    for i in range(10 ** 9 + 1):
        if C[i] != 0:
            print(C[i], end=" ")
    print()

if __name__ == '__main__':
    main()