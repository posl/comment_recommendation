def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(C)
    count = 0
    for i in range(N):
        a = A[i]
        c = C[i]
        #print(a)
        #print(c)
        #print("-----")
        for j in range(N):
            b = B[j]
            #print(b)
            if a < b and b > c:
                count += 1
                #print("count up")
                #print(count)
                #print("-----")
                break
    print(count)

if __name__ == '__main__':
    main()