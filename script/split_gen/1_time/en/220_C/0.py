def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #print("N:", N)
    #print("A:", A)
    #print("X:", X)
    sumA = sum(A)
    #print("sumA:", sumA)
    if sumA > X:
        #print("sumA > X")
        k = 0
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        print(i+1)
    else:
        #print("sumA <= X")
        k = 0
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        #print("i:", i)
        #print("k:", k)
        #print("i+1:", i+1)
        #print("N:", N)
        #print("(i+1)*N:", (i+1)*N)
        #print("k:", k)
        #print("sumA:", sumA)
        k = k + ((X-k)//sumA)*sumA
        #print("k:", k)
        for i in range(N):
            if k > X:
                break
            k += A[i]
            #print("i:", i)
            #print("k:", k)
        print((i+1)+(i+1)*N)
    return
