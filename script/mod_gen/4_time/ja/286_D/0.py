def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    #print(total)
    if total <= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()