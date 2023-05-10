def main():
    N = int(input())
    #print(N)
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        #print(a, b)
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    C = []
    for i in range(N):
        C.append([A[i], B[i]])
    #print(C)
    C.sort(key=lambda x:x[1])
    #print(C)
    now = 0
    for i in range(N):
        now += C[i][0]
        if now > C[i][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()